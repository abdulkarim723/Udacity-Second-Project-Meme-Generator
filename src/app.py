import random
import os
import sys
import requests
from flask import Flask, render_template, request

from ImportEngine.Ingestor import Ingestor
from memeEngine.memeEngine import MemeEngine
from Exceptions import PathNotFound, FileExtensionNotSupported


app = Flask(__name__)

meme = MemeEngine('./static/')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes_ = []

    images_path = "./_data/photos/dog/"
    images = []
    try:
        [quotes_.extend(Ingestor.parse(file)) for file in quote_files]

    except FileExtensionNotSupported or PathNotFound  as e:
        print(e)
        sys.exit(1)
    [images.append(images_path + image) for image in os.listdir(images_path)]

    return quotes_, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    try:
        path = meme.make_meme(img, quote.body, quote.author)
    except PathNotFound as e:
        print(e)
        sys.exit(1)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    try:
        response = requests.get(image_url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    tmp_image = f'./{random.randint(0, 1000)}.png'

    with open(tmp_image, 'wb') as img:
        img.write(response.content)

    author = request.form.get('author')
    quote = request.form.get('body')

    try:
        path = meme.make_meme(tmp_image, quote, author)
    except PathNotFound as e:
        print(e)
        os.remove(tmp_image)
        sys.exit(1)

    os.remove(tmp_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
