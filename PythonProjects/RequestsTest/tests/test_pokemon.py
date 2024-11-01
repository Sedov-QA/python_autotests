import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a534b3f25d073a7f0ec7917fff40138c'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN,}
TRAINER_ID = '8290'
## Проверь, что ответ запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/me', headers = HEADER)
    assert response_get.json()['data'][0]['trainer_name'] == 'ВикторСедов'