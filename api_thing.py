import requests
number = 0
pkmn = input('which pokemon would you like to check? ')
url = f'https://api.pokemontcg.io/v2/cards?q=name:"{pkmn}"'
response = requests.get(url)
pkmns = response.json()
for i in pkmns['data']:
    number = number + 1
print(number)
