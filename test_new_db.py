from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time


def setup_database():
    conn = sqlite3.connect('matches.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS match_stats (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date TEXT, home_team TEXT, away_team TEXT, home_score INTEGER, away_score INTEGER,
                 venue TEXT, attendance INTEGER)''')
    conn.commit()
    conn.close()

# NOTE to add to above db:
# half_time_home_score INTEGER, half_time_away_score INTEGER,home_tries TEXT, away_tries TEXT, home_conversions TEXT, away_conversions TEXT, home_penalty_goals TEXT, away_penalty_goals TEXT


def insert_match_data(match_data):
    conn = sqlite3.connect('matches.db')
    c = conn.cursor()
    c.executemany(
        'INSERT INTO match_stats (date, home_team, away_team, home_score, away_score, venue, attendance) VALUES (?, ?, ?, ?, ?, ?, ?)', match_data)
    conn.commit()
    conn.close()

# NOTE: add to  above insert
# ground_conditions, attendance, half_time_home_score, half_time_away_score, home_tries, away_tries, home_conversions, away_conversions, home_penalty_goals, away_penalty_goals


def scrape_match_data():
    driver = webdriver.Chrome()
    start_time = time.time()

    try:
        url = 'https://www.nrl.com/draw/?competition=111&round=15&season=2024'
        driver.get(url)

        # Use WebDriverWait to wait for the page to load completely
        # WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, '#draw-content section ul li div div a div div.match-header'))
        # )

        matches = driver.find_elements(
            By.CSS_SELECTOR, '#draw-content section ul li div div a div div.match-header')

        if not matches:
            raise ValueError("No match data found on the page")

        match_data_list = []

        for match in matches:
            match_url = match.find_element(
                By.XPATH, '..').get_attribute('href')
            driver.execute_script(
                "window.open(arguments[0], '_blank');", match_url)
            driver.switch_to.window(driver.window_handles[1])

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'match-header__title'))
            )

            # Scrape the required data from the match stats page
            date_element = driver.find_element(
                By.CLASS_NAME, 'match-header__title')
            date = date_element.text.strip() if date_element else 'N/A'

            home_team_element = driver.find_element(
                By.CSS_SELECTOR, '.match-team match-team--home')
            home_team = home_team_element.text.strip() if home_team_element else 'N/A'

            away_team_element = driver.find_element(
                By.CSS_SELECTOR, '.match-team match-team--away')
            away_team = away_team_element.text.strip() if away_team_element else 'N/A'

            home_score_element = driver.find_element(
                By.CSS_SELECTOR, '.match-team__score--home')
            home_score = int(home_score_element.text.strip()
                             ) if home_score_element else 0

            away_score_element = driver.find_element(
                By.CSS_SELECTOR, '.match-team__score--away')
            away_score = int(away_score_element.text.strip()
                             ) if away_score_element else 0

            venue_element = driver.find_element(
                By.CSS_SELECTOR, '.match-venue-broadcasters')
            venue = venue_element.text.strip() if venue_element else 'N/A'

            # Assume the condition as we don't have specific elements
            # ground_conditions = "Slippery"

            attendance_element = driver.find_element(
                By.CSS_SELECTOR, '.match-weather__text')
            attendance = int(attendance_element.text.strip().replace(
                ',', '')) if attendance_element else 0

            # Extract additional stats
            # half_time_score_elements = driver.find_elements(
            #     By.CSS_SELECTOR, '.match-center-summary-group')
            # half_time_home_score = int(
            #     half_time_score_elements[0].text.strip()) if half_time_score_elements else 0
            # half_time_away_score = int(half_time_score_elements[1].text.strip()) if len(
            #     half_time_score_elements) > 1 else 0

            # home_tries = "Sample Home Tries"  # Extract the tries
            # away_tries = "Sample Away Tries"
            # home_conversions = "Sample Home Conversions"
            # away_conversions = "Sample Away Conversions"
            # home_penalty_goals = "Sample Home Penalty Goals"
            # away_penalty_goals = "Sample Away Penalty Goals"

            # append the above list of data plus conditions? to match_data_list when ready - until then they are removed

            match_data_list.append(
                (date, home_team, away_team, home_score, away_score, venue, attendance))

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        return match_data_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed scraping time: {elapsed_time:.2f} seconds")
        driver.quit()


# Setup the database
setup_database()

# Scrape match data and insert into the database
match_data = scrape_match_data()
if match_data:
    insert_match_data(match_data)
    print("Data inserted into the database successfully.")
else:
    print("No match data to insert.")
