import keyfile
import pandas as pd
import numpy as np
import requests
import re

# TESTING STARWARS API
sw_films = requests.get('https://swapi.dev/api/films').text
sw_planets = requests.get('https://swapi.dev/api/planets').text
sw_starships = requests.get('https://swapi.dev/api/starships').text
sw_vehicles = requests.get('https://swapi.dev/api/vehicles').text
# USE CONTEXT MANAGERS TO WRITE TO FILES - they automatically close dependencies after completed action
# for x in range(1,10):
#     sw_people = requests.get('https://swapi.dev/api/people/?page={}'.format(x)).text
#     with open('starwars_people.json', 'a') as f:
#         f.write(sw_people.encode('utf-8'))
# with open('starwars_films.json', 'w') as f:
#     f.write(sw_films.encode('utf-8'))
# with open('starwars_planets.json', 'w') as f:
#     f.write(sw_planets.encode('utf-8'))
# with open('starwars_starships.json', 'w') as f:
#     f.write(sw_starships.encode('utf-8'))
# with open('starwars_vehicles.json', 'w') as f:
#     f.write(sw_vehicles.encode('utf-8'))
# print('Files written successfully.')


# FINANCE API SETUP FOR NUMPY AND PANDAS
income_url = "https://financial-modeling-prep.p.rapidapi.com/income-statement/AAPL"
cashflow_url = "https://financial-modeling-prep.p.rapidapi.com/cash-flow-statement/AAPL"
balance_url = "https://financial-modeling-prep.p.rapidapi.com/balance-sheet-statement/AAPL"
profile_url = "https://financial-modeling-prep.p.rapidapi.com/profile/AAPL"

querystring = {"apikey": "demo"}
headers = {
    'x-rapidapi-host': "financial-modeling-prep.p.rapidapi.com",
    'x-rapidapi-key': keyfile.key
}
income = requests.request(
    "GET", income_url, headers=headers, params=querystring)
cashflow = requests.request(
    "GET", cashflow_url, headers=headers, params=querystring)
balance = requests.request(
    "GET", balance_url, headers=headers, params=querystring)
profile = requests.request(
    "GET", profile_url, headers=headers, params=querystring)

# with open('income.json', 'w') as f:
#     f.write(income.text)
# with open('balancesheet.json', 'w') as f:
#     f.write(balance.text)
# with open('cashflow.json', 'w') as f:
#     f.write(cashflow.text)
# with open('profiles.json', 'w') as f:
#     f.write(profile.text)
# print('Files written successfully.')

# NUMPY AND PANDS MANIPULATION
peeps = pd.read_json("./starwars_people.json")
peep_data = []
for x in peeps.res:
    peep_data += x['results']
peep_df = pd.DataFrame(peep_data)
peep_df.to_csv(path_or_buf='./sw_peeps.csv', index=False, encoding='utf-8')
