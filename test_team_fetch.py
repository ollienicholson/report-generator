import aiohttp
import asyncio
import json
import re
from typing import Dict, List, Any
from cachetools import TTLCache

# Cache setup
cache = TTLCache(maxsize=100, ttl=300)


async def fetch_data(url: str) -> Dict[str, Any]:
    '''Returns a dictionary'''
    if url in cache:
        return cache[url]

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            cache[url] = data
            return data


async def fetch_team_data(data: Dict[str, Any], team_name: str) -> Dict[str, List[Dict[str, str]]]:
    '''Takes a dictionary and returns a team name'''
    # Extract matches involving the given team_name
    # data = json.loads(json_data)
    matches = data.get('NRL', [])
    team_matches: List[Dict[str, str]] = []

    for match_day in matches:
        for match_list in match_day.values():
            for match in match_list:
                if team_name in match['Details']:
                    team_matches.append(match)

    return {team_name: team_matches}


async def main() -> None:
    url = "https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/nrl_data.json"
    json_data = await fetch_data(url)

    # List of team names to fetch data for
    team_names: List[str] = ["Eels", "Storm", "Warriors", "Knights"]

    # Fetch data for each team concurrently
    fetch_tasks = [fetch_team_data(json_data, team_name)
                   for team_name in team_names]
    # NOTE: asyncio.gather(*fetch_tasks) unpacks the list of coroutines to run concurrently
    teams_data: List[Dict[str, List[Dict[str, str]]]] = await asyncio.gather(*fetch_tasks)

    for team_data in teams_data:
        print(team_data)

# Running the asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
