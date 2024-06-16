import json


def save_data(data):
    with open('nrl_data.json', 'w') as file:
        json.dump(data, file, indent=4)
