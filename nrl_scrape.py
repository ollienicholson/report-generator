import requests
from bs4 import BeautifulSoup
import json
from data_storage import save_data

# NOTE on headers
# inspect network > refresh page
# select relevant initiator, in this case [long number].js
# scroll down to Request Headers, retrieve user-agent
# OR
# right-click [long number].js and select copy as cURL
# only user-agent is required as of 17/06/24


def scrape_nrl_data():
    url = 'https://www.nrl.com/draw/?competition=111&round=15&season=2024'

    headers = {
        # 'Origin': 'https://www.nrl.com',
        # 'Referer': 'https://www.nrl.com/draw/?competition=111&round=15&season=2024',
        # 'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        # 'Sec-Ch-Ua-Mobile': '?1',
        # 'Sec-Ch-Ua-Platform': '"Android"',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    # Print first 500 characters of the response text to check
    print(response.text[:100])
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("Soup:", soup)

    games = []

    # Example selectors - these will need to be adjusted to the actual HTML structure
    # Adjust the class name based on actual page structure
    for match in soup.find_all('div', class_='match-info'):
        team_names = [team.get_text() for team in match.find_all(
            'span', class_='team-name')]  # Adjust class names
        # Adjust class names
        date = match.find('div', class_='date-time').get_text()
        # Adjust class names
        score = match.find('div', class_='final-score').get_text()

        games.append({
            'team_1': team_names[0],
            'team_2': team_names[1],
            'date': date.strip(),
            'score': score.strip()
        })

    save_data(games)


if __name__ == "__main__":
    scrape_nrl_data()
