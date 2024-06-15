import json


# get json  data
def load_and_access_data(file_path):
    # open JSON file and load its contents into a dict
    with open(file_path, "r") as file:
        data = json.load(file)

    game_info = data['Stats'][0]['2024']
    game_info = data['Stats']

    return game_info


file_path = "json/testing.json"

test_data = load_and_access_data(file_path)

print("\ntest_data: ", test_data)


# Function to dump data to a JSON file

def dump_data(file_path, data):
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Use json.dump to write data into the file
        json.dump(data, file, indent=4)  # indent=4 for pretty printing

# dump_path = 'output_dump.json'
# dump_data(dump_path, test_data)

# get specific key names from json


def get_key_name(file_path):

    with open(file_path, "r") as file:
        data = json.load(file)

    if 'Stats' in data:
        return 'Stats'

    elif '2024' in data['Stats'][0]:
        return '2024'

    else:
        return "Key 'Stats' not found"
