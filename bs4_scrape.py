import requests
from bs4 import BeautifulSoup

# Fetch the HTML content
url = 'https://www.nrl.com/draw/?competition=111&round=15&season=2024'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,la;q=0.8',
    'Cache-Control': 'no-cache',
    'Cookie': 'optimizelyEndUserId=oeu1710579697153r0.04703023743518675; bitmovin_analytics_uuid=0593f6d8-fa41-4929-a1ae-bdb364fbaa43; ADRUM_BTa=R:0|g:9bca3540-737e-4c6c-a19b-a16f442055b0|n:nrl-prod_65cf7a64-026e-4643-b035-683e13e404ae; SameSite=None',
    'Pragma': 'no-cache',
    'Priority': 'u=2',
    'Referer': 'https://www.nrl.com/draw/?competition=111&round=15&season=2024',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url, headers=headers)

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Locate and extract the data
games = []

# Using the provided structure
matches = soup.select(
    '#draw-content section ul li div div a div div.match-header')
print(matches)
for match in matches:
    match_data = {}

    # Extract date
    date_element = match.find('p', class_='match-header__title')
    if date_element:
        match_data['date'] = date_element.get_text().strip()
        print(date_element)

    # Extract team names
    team_names = [team.get_text().strip()
                  for team in match.find_all('p', class_='match-team__name')]

    # Extract scores
    scores = [score.get_text().strip()
              for score in match.find_all('div', class_='match-team__score')]

    if len(team_names) == 2 and len(scores) == 2:
        match_data['team_1'] = team_names[0]
        match_data['team_2'] = team_names[1]
        match_data['score'] = f'{scores[0]} - {scores[1]}'

    if match_data:
        games.append(match_data)

# Print the list of games with details
for game in games:
    print(game)
