import requests
## Создание покемона (POST /pokemons)
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a534b3f25d073a7f0ec7917fff40138c'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN,}
BODY_SOZDANIE = {
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_SOZDANIE)
print(response_create.text)

massage = response_create.json()['id']
print(massage)

## Смена имени покемона (PUT /pokemons)

BODY_IZMENENIE = {
    "pokemon_id": massage,
    "name": "SEDOV",
    "photo_id": 2
}
response_izmen = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_IZMENENIE)
print(response_izmen.text)

## Поймать покемона в покебол (POST /trainers/add_pokeball)

BODY_POKEBALL = {
    "pokemon_id": massage
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEBALL)
print(response_pokeball.text)