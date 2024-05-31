import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'origin': 'https://www.greggs.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.greggs.co.uk/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'latitude': '50.8229402',
    'longitude': '-0.1362672',
    'distanceInMeters': '48024',
}

response = requests.get('https://production-digital.greggs.co.uk/api/v1.0/shops', params=params, headers=headers)

print(response.text)
