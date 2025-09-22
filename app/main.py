import requests
from app.config import BASE_URL

translation_samples = [
    ('apple', 'es-ES', 'manzana'),
    ('dog', 'de-DE', 'Hund'),
    ('sun', 'jp-JP', '太陽'),
    ('bridge', 'it-IT', 'ponte')
]

ids = ['Apple in Spanish', 
       'Dog in German', 
       'Sun in Japanese', 
       'Bridge in Italian']

def get_translation(query: str, locale: str):
    url = f'{BASE_URL}?query={query}&locale={locale}'
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}



