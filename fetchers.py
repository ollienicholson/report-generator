import requests
import pandas as pd


def fetch_player_data():
    # URL of the JSON data
    url = 'https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/player_statistics_2024.json'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data
        data = response.json()

        # Extract the first player's data
        first_player = data['PlayerStats'][0]['2024'][0]['0'][0]['2024-1-Sea-Eagles-v-Rabbitohs'][0]

        df = pd.DataFrame([first_player])
        return df

    else:
        print("Failed to retrieve data, status code:", response.status_code)
        return None


# NOTE refactor to return only the df and the rest you can do in match_tables.py

def get_match_data(doc):
    url = 'https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/nrl_data.json'

    response = requests.get(url)

    if response.status_code == 200:
        # Load data
        data = response.json()

        for week_data in data['NRL']:
            for week, games in week_data.items():
                doc.add_heading(f"Week {week}", level=2)
                # table = doc.add_table(rows=1, cols=6)
                # hdr_cells = table.rows[0].cells
                # hdr_cells[0].text = 'Match Details'
                # hdr_cells[1].text = 'Date'
                # hdr_cells[2].text = 'Home Team'
                # hdr_cells[3].text = 'Home Score'
                # hdr_cells[4].text = 'Away Team'
                # hdr_cells[5].text = 'Away Score'

                # for game in games:
                #     row_cells = table.add_row().cells
                #     row_cells[0].text = game['Details']
                #     row_cells[1].text = game['Date']
                #     row_cells[2].text = game['Home']
                #     row_cells[3].text = game['Home_Score']
                #     row_cells[4].text = game['Away']
                #     row_cells[5].text = game['Away_Score']
