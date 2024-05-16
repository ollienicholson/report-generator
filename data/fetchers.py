import requests
import pandas as pd
import json


def fetch_player_data():
    '''gets player data in JSON format via API'''
    # URL of the JSON data
    url = 'https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/player_statistics_2024.json'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data
        data = response.json()
        # Open a file for writing (will overwrite if exists)
        with open('json/player_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Extract the first player's data
        first_player = data['PlayerStats'][0]['2024'][0]['0'][0]['2024-1-Sea-Eagles-v-Rabbitohs'][0]

        df = pd.DataFrame([first_player])
        return df

    else:
        print("Failed to retrieve player data, status code:", response.status_code)
        return None


# NOTE refactor to return only the df and the rest you can do in match_tables.py

def fetch_match_data():
    '''
    fetch match data from JSON via API
    potentially want to pass through how many weeks of data you want
    '''
    url = 'https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/nrl_data.json'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
        # # Open a file for writing (will overwrite if exists)
        # with open('json/match_data.json', 'w') as file:
        #     json.dump(data, file, indent=4)

    else:
        print("Failed to retrieve match data, status code:",
              response.status_code)
        return None
