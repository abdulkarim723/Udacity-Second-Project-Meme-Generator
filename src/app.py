import random
import os
import requests
import glob
from PIL import Image
from flask import Flask, render_template, abort, request

from ImportEngine.Ingestor import Ingestor
from memeEngine.memeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static/')


def setup():
    """ Load all resources """

    quote_files = ['./src/_data/DogQuotes/DogQuotesTXT.txt',
                   './src/_data/DogQuotes/DogQuotesDOCX.docx',
                   './src/_data/DogQuotes/DogQuotesPDF.pdf',
                   './src/_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes_ = []

    images_path = "./src/_data/photos/dog/"
    images = []
    try:
        [quotes_.extend(Ingestor.parse(file)) for file in quote_files]

    except Exception as e:
        print(e)
    [images.append(images_path + image) for image in os.listdir(images_path)]

    return quotes_, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    response = requests.get(image_url)

    tmp_image = f'./{random.randint(0, 1000)}.png'

    with open(tmp_image, 'wb') as img:
        img.write(response.content)

    author = request.form.get('author')
    quote = request.form.get('body')

    path = meme.make_meme(tmp_image, quote, author)

    os.remove(tmp_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
