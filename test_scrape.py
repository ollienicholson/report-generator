#
# # # this works as of 5/05/2024
#

import requests

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

    # a. player name, number, position
    player_name = first_player['Name']
    player_number = first_player['Number']
    player_position = first_player['Position']
    print(f"First player from first game in data: \n", player_name,
          "#" + player_number, player_position, "\n")

    # b. PER GAME tries, try assists
    player_tries = first_player['Tries']
    player_try_assists = first_player['Try Assists']
    print("PER GAME: \n"
          "player_tries", player_tries, "\n"
          "player_try_assists", player_try_assists, "\n")

    # c. TOTALS: total points, all run metres, offloads, average play the ball speed, line breaks, passes, on report
    player_total_points = first_player['Total Points']
    player_all_run_metres = first_player['All Run Metres']
    player_total_offloads = first_player['Offloads']
    player_avg_play_ball_speed = first_player['Average Play The Ball Speed']
    player_total_line_breaks = first_player['Line Breaks']
    player_total_passes = first_player['Passes']
    player_total_on_report = first_player['On Report']

    print("TOTALS:", "\n"
          "player_total_points: ", player_total_points, "\n"
          "player_all_run_metres: ", player_all_run_metres, "\n"
          "player_total_offloads: ", player_total_offloads, "\n"
          "player_avg_play_ball_speed: ", player_avg_play_ball_speed, "\n"
          "player_total_line_breaks: ", player_total_line_breaks, "\n"
          "player_total_passes: ", player_total_passes, "\n"
          "player_total_on_report: ", player_total_on_report, "\n")

    # c. AVERAGES: average tries per game (sum of all tries scored divided by number of tries scored)
    if player_tries != '-' and player_total_points != '-':
        avg_tries_per_game = int(player_total_points)/int(player_tries)
        print("avg_tries_per_game: ", avg_tries_per_game)
    else:
        print("Not enough data for average_tries_per_game data\n")

    # points per metre ran
    if player_total_points != '-' and player_all_run_metres != '-':
        avg_points_per_metre = int(
            player_total_points)/int(player_all_run_metres)
        print("avg_points_per_metre: ", round(avg_points_per_metre, 2))
    else:
        print("Not enough data for avg_points_per_metre data\n")

else:
    print("Failed to retrieve data, status code:", response.status_code)
