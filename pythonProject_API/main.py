import requests
import json


url = "https://api.github.com"
username = '5-soldo'

get_response = requests.get(f'{url}/users/{username}/repos')
j_data = get_response.json()
print(j_data)