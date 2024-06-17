import requests
from bs4 import BeautifulSoup
import json
from data_storage import save_data
from lxml import etree

from selenium import webdriver


# NOTE on Request Headers:
# inspect network > refresh page
# select relevant initiator, in this case [long number].js
# scroll down to Request Headers, retrieve user-agent
# OR
# right-click [long number].js and select copy as cURL
# only user-agent is required as of 17/06/24


def scrape_nrl_data():
    url = 'https://www.nrl.com/draw/?competition=111&round=15&season=2024'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,la;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Cache-Control': 'no-cache',
        'Cookie': 'optimizelyEndUserId=oeu1710579697153r0.04703023743518675; bitmovin_analytics_uuid=0593f6d8-fa41-4929-a1ae-bdb364fbaa43; ADRUM_BTa=R:0|g:79eeebe2-5790-4d28-8aa7-b337edb57a38|n:nrl-prod_65cf7a64-026e-4643-b035-683e13e404ae; SameSite=None; ADRUM_BT1=R:0|i:804254|e:12',
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

    # Parse with BeautifulSoup and lxml
    soup = BeautifulSoup(response.text, features='lxml')
    # print(soup.text[:100])

    # Save the parsed HTML to a file
    # with open('scraped_content.html', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

    # print("HTML content has been saved to 'scraped_content.html'")

    tree = etree.HTML(str(soup))

    # Use XPath to find the elements
    # xpath
    # xpath_expr = '//*[@id="draw-content"]/section[1]/ul/li/div/div[1]/a/div/div'
    # xpath_expr = '//*[@id="draw-content"]/section[1]/ul/li/div/div[1]'

    # full - original
    xpath_expr = '/html/body/div[3]/main/div[2]/div[2]/div[2]/div/div[2]/section[1]/ul/li/div/div[1]/a/div/div'

    # Find all matching elements
    elements = tree.xpath(xpath_expr)
    print("elements: ", elements)

    games = []
    print(games)
    for element in elements:
        match_data = {}
        print(match_data)

        # Extract date from the parent div with class 'match-header l-billboard-max-width'
        date_element = element.xpath('.//p[@class="match-header__title"]')
        print('1')
        print(date_element)
        if date_element:
            match_data['date'] = date_element[0].text.strip()

        # Extract team names
        team_names = element.xpath(
            './/p[contains(@class, "match-team__name")]/text()')
        if len(team_names) >= 2:
            match_data['team_1'] = team_names[0].strip()
            match_data['team_2'] = team_names[1].strip()

        # Extract scores
        scores = element.xpath(
            './/div[contains(@class, "match-team__score")]/text()')
        if len(scores) >= 2:
            match_data['score'] = f'{scores[0].strip()} - {scores[1].strip()}'

        games.append(match_data)

    # Print the list of games with details.
    for game in games:
        print(game)


if __name__ == "__main__":
    scrape_nrl_data()


# curl 'https://cdn.optimizely.com/js/26919700052.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-US,en;q=0.9,la;q=0.8' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1' \
#   -H 'referer: https://www.nrl.com/' \
#   -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"' \
#   -H 'sec-ch-ua-mobile: ?1' \
#   -H 'sec-ch-ua-platform: "Android"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: cross-site' \
#   -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'


#   curl 'https://www.nrl.com/Client/dist/nrl.B1299259.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-US,en;q=0.9,la;q=0.8' \
#   -H 'cache-control: no-cache' \
#   -H 'cookie: optimizelyEndUserId=oeu1710579697153r0.04703023743518675; bitmovin_analytics_uuid=0593f6d8-fa41-4929-a1ae-bdb364fbaa43; ADRUM_BTa=R:0|g:9bca3540-737e-4c6c-a19b-a16f442055b0|n:nrl-prod_65cf7a64-026e-4643-b035-683e13e404ae; SameSite=None' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.nrl.com/draw/?competition=111&round=15&season=2024' \
#   -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"' \
#   -H 'sec-ch-ua-mobile: ?1' \
#   -H 'sec-ch-ua-platform: "Android"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
