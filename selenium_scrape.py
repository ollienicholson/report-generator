from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import time
import sqlite3


# NOTE need to traverse through all weeks to scrape historic data
#       - not the same URL, will need to click into each section and scrape from there
def scrape_match_data():

    # Setup WebDriver
    driver = webdriver.Chrome()
    start_time = time.time()  # Start the scraper timer

    try:
        # Open NRL webpage
        url = 'https://www.nrl.com/draw/?competition=111&round=15&season=2024'
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(5)  # Adjust the sleep time as needed

        # Find and print the match elements
        matches = driver.find_elements(
            By.CSS_SELECTOR, '#draw-content section ul li div div a div div.match-header')
        if not matches:
            raise ValueError("No match data found on the page")

        match_data_list = []
        for match in matches:
            date_element = match.find_element(
                By.CLASS_NAME, 'match-header__title')
            date = date_element.text.strip() if date_element else 'N/A'

            team_names = [team.text.strip() for team in match.find_elements(
                By.CLASS_NAME, 'match-team__name')]
            scores = [score.text.strip() for score in match.find_elements(
                By.CLASS_NAME, 'match-team__score')]

            print(f"Match date: {date} \n")
            if len(team_names) == 2 and len(scores) == 2:
                match_data_list.append(
                    (date, team_names[0], team_names[1], scores[0], scores[1]))

        return match_data_list

    except Exception as e:
        print("there was an error:", {e})
        return []

    finally:
        end_time = time.time()  # End the timer
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Elapsed scraping time: {elapsed_time:.2f} seconds")

        # Close the browser
        driver.quit()


def setup_database():
    conn = sqlite3.connect('matches.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS matches
              (date TEXT, team_1 TEXT, team_2 TEXT, score_1 INTEGER, score_2 INTEGER)''')
    conn.commit()
    conn.close()


def insert_data(match_data):
    conn = sqlite3.connect('matches.db')
    c = conn.cursor()
    c.executemany(
        'INSERT INTO matches (date, team_1, team_2, score_1, score_2) VALUES (?,?,?,?,?)', match_data)
    conn.commit()
    conn.close()


setup_database()
match_data = scrape_match_data()

if match_data:
    insert_data(match_data)
    print("Data inserted into matches.db successfully")
else:
    print("No match data to insert")
