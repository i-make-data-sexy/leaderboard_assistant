# ========================================================================
#   Imports
# ========================================================================

# ===============================
#   Standard Libraries
# ===============================
import re
import logging
import time

# ===============================
#   Selenium WebDriver
# ===============================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# ===============================
#   App
# ===============================

from recommendations_engine import RECOMMENDATIONS

# ===============================
#   Misc
# ===============================

import streamlit as st


# ========================================================================
#   Logging
# ========================================================================

# Set up logging
logging.basicConfig(
    filename="search_debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# ========================================================================
#   Set Up Streamlit App
# ========================================================================

# Set page title
st.title("AI Model Leaderboard Search with Debugging")

# Search input
search_term = st.text_input("Enter model name (e.g., 'Phi-4' or 'Claude')")

# Task filter
task_options = list(RECOMMENDATIONS.keys())
selected_task = st.selectbox("Select a task:", options=task_options)



# ========================================================================
#   Set up Selenium WebDriver
# ========================================================================

def get_driver():
    """
    Initializes and returns a Selenium WebDriver.
    Returns:
        WebDriver: An instance of a Selenium WebDriver.
    """
    service = Service('/usr/local/bin/chromedriver')  # Replace with your chromedriver path
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")  # Set viewport size
    return webdriver.Chrome(service=service, options=options)

def is_model_on_leaderboard(url, model_name):
    """
    Checks if a given model name exists on a specified leaderboard URL using Selenium.

    Args:
        url (str): The URL of the leaderboard to search.
        model_name (str): The name of the model to search for.

    Returns:
        dict: A dictionary containing search results. 
              - "found" (bool): True if the model name (or a close variant) is found, False otherwise.
              - "match_type" (str): "exact" if the model name is an exact match, "variant" if a close variant is found, 
                                  "timeout" if a timeout occurred, or "error" if another error occurred, otherwise None.
              - "matched_text" (str): The actual text that matched on the leaderboard (if found), or None.
    """
    # Initialize driver variable outside try block
    driver = None  
    
    # Outer try-except block for driver initialization and critical errors.
    try:
        driver = get_driver()

        max_retries = 3
        retry_count = 0

        # Set retry logic
        while retry_count < max_retries:  # Retry up to max_retries times
            # Main try-except block for Selenium interactions and page loading.
            try:
                # Log start of search
                logging.info(f"\n{'=' * 50}\nStarting search for '{model_name}' on {url}\n{'=' * 50}")
                
                # Navigate to the provided leaderboard URL
                driver.get(url)

                # Initialize WebDriverWait with a 60-second timeout
                wait = WebDriverWait(driver, 60)  # Set up wait with 60-second timeout

                # Inner try-except block specifically for handling timeout exceptions during wait conditions.
                try:
                    # Site-specific wait conditions for improved handling of dynamic content:
                    
                    # Chatbot Arena
                    if "lmarena.ai" in url:  
                        # Find div table is nested in
                        locator = (By.XPATH, "//div[contains(@class, 'svelte')]/table/tbody/tr")
                        
                        # Wait for leaderboard rows to load
                        wait.until(EC.presence_of_all_elements_located(locator))  
                        logging.debug("Chatbot Arena Leaderboard rows found.")  # Log success

                    # Hugging Face (adjust XPATH if needed)
                    elif "huggingface.co" in url:  
                        # Find div table is nested in
                        locator = (By.XPATH, "//div[contains(@class, 'MuiTableContainer')]/table/tbody/tr")
                        
                        # Wait for model links to be present
                        wait.until(EC.presence_of_all_elements_located(locator))  
                        
                        # Log success
                        logging.debug("Hugging Face Model links found.")  

                    else:  # Generic wait condition for other sites
                    
                        # 1. Wait for the table element to be present (indicating page structure is loaded)
                        wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

                        # 2. Wait for at least 10 table rows (<tr>) to be present, assuming data has loaded
                        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//table//tr")) >= 10)
                        logging.debug("Minimum 10 rows found")


                        # Extract text from all table cells (<td>) and links (<a>) within those cells
                        cells = driver.find_elements(By.TAG_NAME, "td")
                        logging.info(f"Found {len(cells)} table cells")

                        if not cells: # Check for empty cell list
                            logging.warning("Table cells found but are empty.")  # Log warning if cells are found but empty
                            return {"found": False, "match_type": None, "matched_text": None}
                        
                        cell_contents = []
                        
                        # Loop through each cell to extract text and link information.
                        for cell in cells:
                            cell_text = cell.text.strip()
                            if cell_text:
                                cell_contents.append(cell_text.lower())

                            # Extract links within the cell
                            links = cell.find_elements(By.TAG_NAME, "a")  
                            
                            # Iterate through each link
                            for link in links:  
                                # Extract link text if exists
                                link_text = link.text.strip()   
                                if link_text:
                                    cell_contents.append(link_text.lower())

                                # Get the URL from the href attribute, if it exists
                                href = link.get_attribute("href")    
                                if href:
                                    # Add href if exists and normalize case
                                    cell_contents.append(href.lower())    
                        
                        # Combine extracted text. Normalize case
                        content_text = " ".join(cell_contents).lower() # Combine cell and link text for searching. Normalize case

                        # Normalize search term for matching
                        normalized_model_name = model_name.lower().strip()

                        # List of regex patterns for matching model name
                        patterns = [  
                            f"\\b{re.escape(normalized_model_name)}\\b",  # Exact word match (whole word)
                            f"\\b{re.escape(normalized_model_name)}[\\-_.]?\\d*\\b",  # Exact match with optional suffix (e.g., GPT-3.5-turbo)
                            f"\\b\\w*{re.escape(normalized_model_name)}\\w*\\b",  # Partial match 
                            f"[/=]{re.escape(normalized_model_name)}[\\-_/]"  # Match model name in URL paths
                        ]

                        # Iterate over each match pattern to look for increasingly fuzzy matches
                        for pattern in patterns:  
                            # Case-insensitive regex search
                            if re.search(pattern, content_text, re.IGNORECASE): 
                                # Extract matched text 
                                matched_text = re.search(pattern, content_text, re.IGNORECASE).group(0)
                                return {  # Model (or a variant) found; return match details
                                    "found": True,
                                    "match_type": "exact" if matched_text.lower() == normalized_model_name else "variant",
                                    "matched_text": matched_text
                                }
                        
                        # Model not found after all pattern checks
                        return {"found": False, "match_type": None, "matched_text": None}  

                # Handle timeout exception during wait
                except TimeoutException: 
                    logging.warning("Timeout waiting for leaderboard data")
                    if retry_count < max_retries - 1:
                        logging.warning(f"Retrying {url}...")
                    return {"found": False, "match_type": "timeout", "matched_text": None}

            # Handle other Selenium exceptions
            except Exception as e:  
                retry_count += 1
                # Log the error for debugging
                logging.error(f"Attempt {retry_count} failed: {e}")  
                
                # Retry with exponential backoff
                if retry_count < max_retries:  
                    time.sleep(2**retry_count)
                    
                    logging.error(f"All {max_retries} attempts failed")
                    return {"found": False, "match_type": "error", "matched_text": None}


    except Exception as e:  # Handle driver initialization or other critical errors
        logging.error(f"Critical error: {e}")
        return {"found": False, "match_type": "error", "matched_text": None}  # Indicate an error

    finally:  # Ensure driver cleanup
        if driver:  # If driver exists (even after error), attempt to close the browser
            driver.quit()
            logging.info("Browser session closed")
            logging.info(f"\n{'=' * 50}\nSearch completed\n{'=' * 50}")


# ========================================================================
#   Streamlit Search Logic
# ========================================================================

# Search button logic
if st.button("Search"):
    # Check if user provided a model name
    if search_term:  
        # Display spinner while searching
        with st.spinner(f"Searching for '{search_term}'..."): 
            # Safely access leaderboards 
            leaderboards = RECOMMENDATIONS.get(selected_task, {}).get('Quality', []) 

            found_any = False
            if leaderboards:
                for board in leaderboards:
                    board_name = board['leaderboard']
                    board_abbrev = board['leaderboard_abbrev']
                    board_link = board['leaderboard_link']['url']

                    # Search each leaderboard in turn
                    result = is_model_on_leaderboard(board_link, search_term) 
                    

                    if result["found"]:
                        # Set flag if any leaderboard matches
                        found_any = True 

                        # Display appropriate message based on match_type
                        if result["match_type"] == "exact": 
                            st.success(f"**{board_name} ({board_abbrev})**: Exact match found! [Visit Leaderboard]({board_link})")
                        else:
                            st.info(f"**{board_name} ({board_abbrev})**: Possible match found (verify manually) [Visit Leaderboard]({board_link})")

                    elif result['match_type'] == 'timeout': # Handle and display timeout message for each leaderboard individually.
                        st.warning(f"**{board_name} ({board_abbrev})**: Timeout. Model may or may not be present. [Verify here]({board_link})")
                    else:
                        st.warning(f"**{board_name} ({board_abbrev})**: Model not found. [Verify here]({board_link})")

            # Display message if no leaderboards for the task, or task does not exist
            else: 
                st.warning(f"No 'Quality' leaderboards found for '{selected_task}'.")
        
        # Display overall message if no matches are found after all leaderboards are checked
        if not found_any: 
             st.info("No leaderboards matched your search. Please verify the links above.")

    #  Display message if no search term is provided
    else:  
        st.warning("Please enter a model name to search.")