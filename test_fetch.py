import aiohttp
import asyncio
from cachetools import TTLCache

# Cache setup
# Cache with max size 100 and TTL 5 minutes
cache = TTLCache(maxsize=100, ttl=300)


async def fetch_data(url):
    if url in cache:
        return cache[url]

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            cache[url] = data
            return data


async def fetch_team_data():
    '''
    TODO: pass team name
    '''
    url = "https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/nrl_data.json"
    return await fetch_data(url)


async def fetch_player_data():
    ''''
    TODO: pass player data'''
    url = f"https://geo145327-staging.s3.ap-southeast-2.amazonaws.com/public/player_statistics_2024.json"
    return await fetch_data(url)

# Example usage


async def main():
    team_id = "example_team_id"
    player_id = "example_player_id"
    team_data = await fetch_team_data()
    player_data = await fetch_player_data()
    print("TEAM DATA:\n", team_data)
    print("PLAYER DATA:\n", player_data)

if __name__ == "__main__":
    asyncio.run(main())
