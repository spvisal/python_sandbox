import requests
import json
import pandas as pd


url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2020014"

headers = {
  'authority': 'api.afl.com.au',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'accept': 'application/json',
  'x-media-mis-token': '83644a2b97ea05be725ea718e6c02da2',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
  'content-type': 'application/x-www-form-urlencoded',
  'origin': 'https://www.afl.com.au',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.afl.com.au/',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'if-none-match': 'W/"e8d55e95a5b88be16648721f57b485f9"',
  'Cookie': 'JSESSIONID=9BC9BF6FB691027BF1D76D64DCF4396B'
}

response = requests.get(url, headers=headers)

playerdata = response.json()

df= pd.json_normalize(playerdata['players'])

df.to_csv('playersdata.csv', index=False)