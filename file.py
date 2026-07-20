import requests



endpoints = 'https://official-joke-api.appspot.com/random_joke'

try:
    response = requests.get(endpoints)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:print(f'Error {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error {e}')