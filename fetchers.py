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
