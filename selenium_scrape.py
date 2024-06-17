from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_data():
    # Setup WebDriver
    driver = webdriver.Chrome()
    try:
        # Open the webpage
        url = 'https://www.nrl.com/draw/?competition=111&round=15&season=2024'
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(10)  # Adjust the sleep time as needed

        # Find and print the match elements
        matches = driver.find_elements(
            By.CSS_SELECTOR, '#draw-content section ul li div div a div div.match-header')
        if not matches:
            raise ValueError("No match data found on the page")

        for match in matches:
            date_element = match.find_element(
                By.CLASS_NAME, 'match-header__title')
            date = date_element.text.strip() if date_element else 'N/A'

            team_names = [team.text.strip() for team in match.find_elements(
                By.CLASS_NAME, 'match-team__name')]
            scores = [score.text.strip() for score in match.find_elements(
                By.CLASS_NAME, 'match-team__score')]

            print(f"Date: {date}")
            if len(team_names) == 2:
                print(f"Teams: {team_names[0]} vs {team_names[1]}")
            if len(scores) == 2:
                print(f"Score: {scores[0]} - {scores[1]}")
    except Exception as e:
        print("there was an error:", {e})

    finally:
        # Close the browser
        driver.quit()


# Call the function to fetch match data
scrape_data()
