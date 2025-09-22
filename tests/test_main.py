import pytest
import logging
from unittest.mock import patch, MagicMock
from app.main import get_translation, translation_samples, ids

logging.basicConfig(level=logging.INFO)

@patch('app.main.requests.get')
@pytest.mark.parametrize('query, locale, expected', 
                         translation_samples, 
                         ids=ids)
def test_get_translation(mock_get, query, locale, expected):
    logging.info(f'Translation of the word "{query}" into {locale}.')
    mock_response = MagicMock()
    mock_response.json.return_value = expected
    mock_get.return_value = mock_response
    result = get_translation(query, locale)
    assert result == expected


