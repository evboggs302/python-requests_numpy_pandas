
import re
import requests
import numpy as np
import pandas as pd

# people/    films/    planets/   starships/   vehicles/
x = requests.get('https://swapi.dev/api/films/3').text

print(x)
