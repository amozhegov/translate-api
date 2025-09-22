import requests
from app.config import BASE_URL


# Sample translation data used for testing
# Each tuple contains: (word to translate, locale code, expected translation)
translation_samples = [
    ('apple', 'es-ES', 'manzana'),
    ('dog', 'de-DE', 'Hund'),
    ('sun', 'jp-JP', '太陽'),
    ('bridge', 'it-IT', 'ponte')
]

# List of human-readable IDs for tests (used in pytest parameterized tests)
ids = ['Apple in Spanish', 
       'Dog in German', 
       'Sun in Japanese', 
       'Bridge in Italian']

# Function to get a translation from the API
#   query: the word to translate
#   locale: the language code to translate into 
def get_translation(query: str, locale: str):
    url = f'{BASE_URL}?query={query}&locale={locale}'
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}



