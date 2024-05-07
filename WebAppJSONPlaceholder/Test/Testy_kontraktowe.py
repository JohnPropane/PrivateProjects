import pytest
import web_functions
# pip install requests-mock
import requests_mock

@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m

# Testowanie funkcji generate_posts
def test_generate_posts(mock_requests):
    # Mockowanie odpowiedzi dla konkretnych adresów URL
    mock_requests.get('https://jsonplaceholder.typicode.com/posts',
                      json=[{"id": 1,
                             "title": "title1",
                             "body": "body1"}])
    mock_requests.get('https://jsonplaceholder.typicode.com/comments',
                      json=[{"postId": 1,
                             "email": "email1",
                             "body": "body1",
                             "name": "name1"}])
    # Wywołanie testowanej funkcji
    posts = web_functions.generate_posts(1)
    # Sprawdzenie wyników
    assert len(posts) == 1
    assert posts[0][0] == "title1"
    assert posts[0][1] == "body1"
    assert posts[0][2][0][0] == "email1"
    assert posts[0][2][0][1] == "body1"
    assert posts[0][2][0][2] == "name1"

# Testowanie funkcji generate2
def test_generate2():
    # Wywołanie testowanej funkcji
    posts = web_functions.generate2(1, 0, 1000)
    # Sprawdzenie wyników
    assert len(posts) == 2
    assert posts[-1] == 1

# Testowanie funkcji generate_albums
def test_generate_albums(mock_requests):
    # Mockowanie odpowiedzi dla konkretnego adresu URL
    mock_requests.get('https://jsonplaceholder.typicode.com/albums',
                      json=[{"id": 1,
                             "title": "title1"}])
    # Wywołanie testowanej funkcji
    albums = web_functions.generate_albums(1)
    # Sprawdzenie wyników
    assert len(albums) == 1
    assert albums[0][0] == 1
    assert albums[0][1] == "title1"

# Testowanie funkcji generate_thumb
def test_generate_thumb(mock_requests):
    # Mockowanie odpowiedzi dla konkretnego adresu URL
    mock_requests.get('https://jsonplaceholder.typicode.com/photos',
                      json=[{"thumbnailUrl": "url1"},
                            {"thumbnailUrl": "url2"},
                            {"thumbnailUrl": "url3"}])
    # Wywołanie testowanej funkcji
    thumbs = web_functions.generate_thumb(1)
    # Sprawdzenie wyników
    assert len(thumbs) == 1
    assert thumbs[0][0] == "url1"
    assert thumbs[0][1] == "url2"
    assert thumbs[0][2] == "url3"


# Testowanie funkcji generate_photos
def test_generate_photos(mock_requests):
    # Mockowanie odpowiedzi dla konkretnego adresu URL
    mock_requests.get('https://jsonplaceholder.typicode.com/photos',
                      json=[{"albumId": 1,
                             "title": "title1",
                             "url": "url1",
                             "thumbnailUrl": "thumb1"}])
    # Wywołanie testowanej funkcji
    photos = web_functions.generate_photos(1, 1)
    # Sprawdzenie wyników
    assert len(photos) == 1
    assert photos[0][0] == "title1"
    assert photos[0][1] == "url1"
    assert photos[0][2] == 1
    assert photos[0][4] == "thumb1"
