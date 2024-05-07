import unittest
from unittest.mock import patch
import web_functions as web


# Definiowanie klasy testowej
class TestWeb(unittest.TestCase):

    # Testowanie funkcji generate_post z mockowaną funkcją requests.get
    @patch('web_functions.requests.get')
    def test_generate_post(self, mock_get):
        # Definiowanie mockowanych odpowiedzi
        mock_response_posts = [{"id": 1, "title": "Title 1", "body": "Body 1"},
                               {"id": 2, "title": "Title 2", "body": "Body 2"}]
        mock_response_comments = [{"postId": 1, "email": "email1@example.com", "body": "Comment 1", "name": "Name 1"},
                                  {"postId": 2, "email": "email2@example.com", "body": "Comment 2", "name": "Name 2"}]
        # Ustawienie mockowanych odpowiedzi jako wyników funkcji requests.get
        mock_get.side_effect = [
            unittest.mock.Mock(json=unittest.mock.Mock(return_value=mock_response_posts)),
            unittest.mock.Mock(json=unittest.mock.Mock(return_value=mock_response_comments))
        ]
        # Wywołanie testowanej funkcji
        generated_posts = web.generate_posts(2)
        # Definiowanie oczekiwanych wyników
        expected_posts = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2]
        ]
        # Porównanie wyników
        self.assertEqual(generated_posts, expected_posts)

    # Testowanie funkcji generate2 z mockowaną funkcją generate_posts
    @patch('web_functions.generate_posts')
    def test_generate2(self, mock_generate_posts):
        # Ustawienie mockowanej odpowiedzi
        mock_generate_posts.return_value = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2]
        ]
        # Wywołanie testowanej funkcji i porównanie wyników
        self.assertEqual(web.generate2(10, 1001, 1000), "Error1")
        self.assertEqual(web.generate2(101, 0, 1000), "Error2")
        # Definiowanie oczekiwanych wyników
        expected_posts = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2],
            2
        ]
        # Wywołanie testowanej funkcji i porównanie wyników
        self.assertEqual(web.generate2(2, 0, 1000), expected_posts)
        self.assertEqual(web.generate2(3, 0, 1000), expected_posts)

    # Testowanie funkcji generate_albums z mockowaną funkcją requests.get
    @patch('web_functions.requests.get')
    def test_generate_albums(self, mock_get):
        # Ustawienie mockowanej odpowiedzi
        mock_response = [{"id": 1, "title": "Album 1"},
                         {"id": 2, "title": "Album 2"},
                         {"id": 3, "title": "Album 3"}]
        mock_get.return_value.json.return_value = mock_response
        # Wywołanie testowanej funkcji
        result = web.generate_albums(3)
        # Definiowanie oczekiwanych wyników
        expected = [[1, "Album 1"], [2, "Album 2"], [3, "Album 3"]]
        # Porównanie wyników
        self.assertEqual(result, expected)

    # Testowanie funkcji generate_photos z mockowaną funkcją requests.get
    @patch('web_functions.requests.get')
    def test_generate_photos(self, mock_get):
        # Ustawienie mockowanej odpowiedzi
        mock_response = [
            {"albumId": 1, "title": "Photo 1", "url": "url1", "thumbnailUrl": "thumbnail1"},
            {"albumId": 1, "title": "Photo 2", "url": "url2", "thumbnailUrl": "thumbnail2"},
            {"albumId": 2, "title": "Photo 3", "url": "url3", "thumbnailUrl": "thumbnail3"}
        ]
        mock_get.return_value.json.return_value = mock_response
        # Wywołanie testowanej funkcji
        album_id = 1
        num_of_photos = 2
        result = web.generate_photos(album_id, num_of_photos)
        # Definiowanie oczekiwanych wyników
        expected_photos = [
            ["Photo 1", "url1", 1, "button0", "thumbnail1"],
            ["Photo 2", "url2", 1, "button1", "thumbnail2"]
        ]
        # Porównanie wyników
        self.assertEqual(result, expected_photos)
