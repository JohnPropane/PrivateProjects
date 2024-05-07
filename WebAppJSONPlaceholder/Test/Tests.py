import unittest
from unittest.mock import patch
from flask import request
import web_functions
from main import app


# Definiowanie klasy testów
class Tests(unittest.TestCase):

    # Metoda setUp jest wywoływana przed każdym testem
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Testowanie trasy domowej
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Testowanie trasy postów z mockowaną funkcją generate2
    @patch('web_functions.generate2')
    def test_posts_route(self, mock_generate2):
        # Ustawienie wartości zwracanej przez mockowaną funkcję
        mock_generate2.return_value = [{'title': 'Post 1', 'content': 'Content 1'},
                                       {'title': 'Post 2', 'content': 'Content 2'}]
        # Wywołanie trasy i sprawdzenie kodu odpowiedzi
        response = self.app.post('/posts', data={'max-posts': '10', 'min-len': '5', 'max-len': '10'})
        self.assertEqual(response.status_code, 200)

    # Testowanie trasy zdjęć z mockowaną funkcją generate_photos
    @patch('web_functions.generate_photos')
    def test_photos_route(self, mock_generate_photos):
        # Ustawienie wartości zwracanej przez mockowaną funkcję
        mock_generate_photos.return_value = [{'title': 'Photo 1'}, {'title': 'Photo 2'}]
        # Wywołanie trasy i sprawdzenie kodu odpowiedzi
        response = self.app.post('/albums/photos/1', data={'max-posts': '10'})
        self.assertEqual(response.status_code, 200)


# Uruchomienie testów
if __name__ == '__main__':
    unittest.main()
