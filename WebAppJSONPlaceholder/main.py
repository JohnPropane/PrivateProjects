from flask import Flask, render_template, request
import web_functions
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    try:
        if request.method == 'POST':
            num_of_posts = int(request.form['max-posts'])
            min_len = int(request.form['min-len'])
            max_len = int(request.form['max-len'])
            data = web_functions.generate2(num_of_posts, min_len, max_len)
        else:
            num_of_posts = 100
            data = web_functions.generate2(num_of_posts)
        return render_template('posts.html', data=data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise e


@app.route('/albums/', methods=['GET', 'POST'])
def albums():
    try:
        if request.method == 'POST':
            num_of_albums = int(request.form['max-posts'])
            data = web_functions.generate_albums(num_of_albums)
            thumbs = web_functions.generate_thumb(num_of_albums)
        else:
            data = web_functions.generate_albums()
            thumbs = web_functions.generate_thumb()
        return render_template('albums.html', data=data, thumbs=thumbs)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise e


@app.route('/albums/photos/<id_1>', methods=['GET', 'POST'])
def photos(id_1):
    try:
        if request.method == 'POST':
            num_of_photos = int(request.form['max-posts'])
            data = web_functions.generate_photos(id_1, num_of_photos)
        else:
            data = web_functions.generate_photos(id_1)
        return render_template('photos.html', data=data, id_1=id_1)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise e


if __name__ == '__main__':
    app.run(debug=True)
