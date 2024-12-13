# ========================================================================
#   Imports
# ========================================================================

from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
import logging
import os
from recommendations_engine import QUESTIONS, RECOMMENDATIONS

# ========================================================================
#   Logging
# ========================================================================

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# ========================================================================
#   App Config
# ========================================================================

# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Configure secret key
app.secret_key = os.getenv('AI_LEAD_FLASK_SECRET_KEY', 'default_secret_key')  

app.config['SESSION_TYPE'] = 'filesystem'

# ========================================================================
#   Routes
# ========================================================================

# Home Route
@app.route('/')
def index():
    session.clear()  # Clear previous session data
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)