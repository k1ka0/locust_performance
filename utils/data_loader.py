import json
import random

def get_payload(key):
    # Carrega o arquivo (em um cenário real, isso pode vir de um banco ou arquivo grande)
    with open('data/payloads.json', 'r') as f:
        data = json.load(f)
    return data.get(key)

def get_random_post_id():
    # Retorna um ID aleatório entre 1 e 100 (limite do JSONPlaceholder)
    return random.randint(1, 100)
