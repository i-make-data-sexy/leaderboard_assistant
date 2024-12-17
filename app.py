# ========================================================================
#   Imports
# ======================================================================== 

from flask import Flask, render_template, request, redirect, url_for, session, jsonify 
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
import logging
import os
from recommendations_engine import QUESTIONS, RECOMMENDATIONS

# From NH 
import pandas as pd
from pyvis.network import Network
from processing import build_network
from bs4 import BeautifulSoup

# ========================================================================
#   Set Up App
# ======================================================================== 

# Initialize the Flask app
app = Flask(__name__)

# ========================================================================
#   Routes
# ========================================================================

# Home Route
@app.route('/')
def index():
    # Read the CSV file
    df = pd.read_csv('input/airtable_20241115.csv')
    
    # Convert df to JSON-safe format
    df = df.fillna('')
    data = df.to_dict(orient='records')
    
    # Build the network graph
    net = build_network(df)
    net.cdn_resources = 'remote'
    
    # Generate the network graph HTML
    graph_html = net.generate_html(notebook=False)
    soup = BeautifulSoup(graph_html, 'html.parser')
    
    # Clean up canvas
    canvas = soup.find('canvas')
    if canvas:
        for attr in ['width', 'height', 'style']:
            if attr in canvas.attrs:
                del canvas[attr]
                
    # Clean up divs
    for div in soup.find_all('div'):
        if 'style' in div.attrs:
            del div['style']
            
    # Extract scripts and modify network initialization
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and 'var network = new vis.Network' in script.string:
            # Move network initialization to a global function
            script.string = '''
                function initNetwork() {
                    window.network = new vis.Network(
                        document.getElementById("mynetwork"),
                        {nodes: new vis.DataSet(%s), edges: new vis.DataSet(%s)},
                        %s
                    );
                    
                    network.once('stabilizationIterationsDone', function() {
                        network.setOptions({physics: false});
                    });
                }
                
                // Call initNetwork after document is ready
                document.addEventListener('DOMContentLoaded', initNetwork);
            ''' % (
                net._nodes.to_json(),
                net._edges.to_json(),
                json.dumps(net.options)
            )
    
    # Extract body and scripts
    graph_body = str(soup.body)
    graph_scripts = ''.join([str(script) for script in scripts])
    
    return render_template(
        'network.html',
        graph_body=graph_body,
        graph_scripts=graph_scripts,
        initialData=json.dumps(data)  # Serialize data to JSON string
    )

# Question Route
@app.route('/question/<key>', methods=['GET', 'POST'])
def question(key):
    # Check if key exists in QUESTIONS
    if key not in QUESTIONS:
        return redirect(url_for('index'))

    question_data = QUESTIONS[key]

    # Form for the current question
    class QuestionForm(FlaskForm):
        choice = RadioField(
            question_data["question"],
            choices=[(option, option) for option in question_data["options"]],
            render_kw={"class": "form-check-input"}
        )
        submit = SubmitField('Next')

    form = QuestionForm()

    # Handle form submission
    if form.validate_on_submit():
        session[key] = form.choice.data  # Save the choice in the session
        next_key = question_data.get("next")
        if next_key == "recommendation":
            return redirect(url_for('recommendation'))
        return redirect(url_for('question', key=next_key))

    return render_template('question.html', form=form, key=key, question_data=question_data)

# Recommendation Route
@app.route('/recommendation')
def recommendation():
    task = session.get("task")
    goal = session.get("goal")
    if not task or not goal:
        return redirect(url_for('index'))

    recommendations = RECOMMENDATIONS.get(task, {}).get(goal, [])
    return render_template(
        'recommendation.html',
        recommendations=recommendations,
        task=task,
        goal=goal
    )
