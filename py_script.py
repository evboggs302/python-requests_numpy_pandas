import keyfile
import pandas as pd
import numpy as np
import requests
import re

# Testing requests with Star Wars api.
sw_people = requests.get('https://swapi.dev/api/people/?page=9').text
# sw_films = requests.get('https://swapi.dev/api/films').text
# sw_planets = requests.get('https://swapi.dev/api/planets').text
# sw_starships = requests.get('https://swapi.dev/api/starships').text
# sw_vehicles = requests.get('https://swapi.dev/api/vehicles').text
# USE CONTEXT MANAGERS TO WRITE TO FILES - they automatically close dependencies after completed action
with open('starwars_people.json', 'a') as f:
    f.write(sw_people.encode('utf-8'))
# with open('starwars_films.json', 'w') as f:
#     f.write(sw_films.encode('utf-8'))
# with open('starwars_planets.json', 'w') as f:
#     f.write(sw_planets.encode('utf-8'))
# with open('starwars_starships.json', 'w') as f:
#     f.write(sw_starships.encode('utf-8'))
# with open('starwars_vehicles.json', 'w') as f:
#     f.write(sw_vehicles.encode('utf-8'))
# print('Files written successfully.')


# Finance API to eventually use NumPy and Pandas.
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
