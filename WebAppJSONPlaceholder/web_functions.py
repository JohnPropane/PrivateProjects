import requests

URL = "https://jsonplaceholder.typicode.com"


def generate_posts(num_of_posts):
    data = requests.get(f"{URL}/posts").json()
    comments_data = requests.get(f"{URL}/comments").json()
    posts = []
    for i in range(num_of_posts):
        id_post = data[i]["id"]
        title = data[i]["title"]
        body = data[i]["body"]
        comments = []
        for j in range(len(comments_data)):
            if comments_data[j]["postId"] == id_post:
                comment = [comments_data[j]["email"],
                           comments_data[j]["body"],
                           comments_data[j]["name"]]
                comments.append(comment)
        posts.append([title, body, comments, id_post])
    return posts


def generate2(num_of_posts, min_len=0, max_len=1000):
    if min_len > max_len:
        return "Error1"
    if not 0 <= num_of_posts <= 100:
        return "Error2"
    data = generate_posts(100)
    generated_posts = 0
    posts = []
    for post in data:
        post_len = len(post[1])
        if min_len <= post_len <= max_len:
            posts.append(post)
            generated_posts += 1
            if generated_posts == num_of_posts:
                posts.append(generated_posts)
                return posts
    posts.append(generated_posts)
    return posts


def generate_albums(num_of_albums=100):
    data = requests.get(f"{URL}/albums").json()
    albums = []
    for i in range(num_of_albums):
        album_id = data[i]["id"]
        album_title = data[i]["title"]
        albums.append([album_id, album_title])
    return albums


def generate_thumb(num_of_albums=100):
    data = requests.get(f"{URL}/photos").json()
    thumbs = []
    for i in range(0, num_of_albums*50, 50):
        thumbs.append([data[i]["thumbnailUrl"],
                       data[i + 1]["thumbnailUrl"],
                       data[i + 2]["thumbnailUrl"]])
    return thumbs


def generate_photos(albumid, num_of_photos=50):
    data = requests.get(f"{URL}/photos").json()
    photos = []
    for i in range(len(data)):
        if num_of_photos == len(photos):
            return photos
        if int(data[i]["albumId"]) == int(albumid):
            album_id = data[i]["albumId"]
            photo_title = data[i]["title"]
            photo_url = data[i]["url"]
            button_id = f"button{i}"
            thumbnail = data[i]["thumbnailUrl"]
            photos.append([photo_title,
                           photo_url,
                           album_id,
                           button_id,
                           thumbnail])
    return photos
