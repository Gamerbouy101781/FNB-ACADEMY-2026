import requests



endpoints = 'http://universities.hipolabs.com/search?country=South+Africa'

try:
    response = requests.get(endpoints)
    if response.status_code == 200:
        data = response.json()
        #print(data)
    else:print(f'Error {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error {e}')


print("===================================================================")
print("           List of Universities in South Africa")
print("===================================================================")
search = input("Search: ")
print("")
for information in data:
    if information['name'] == search:
        print(f'Name: {information['name']}')
        print(f'Province: {information['state-province']}')
        print(f'Website: {information['web_pages'][0]}')
        print(f'Domains: {information['domains'][0]}')
        print(f'Country code: {information['alpha_two_code']}')
        print(f'Country: {information['country']}')
        print("===================================================================")


#print(data[0]['name'])

