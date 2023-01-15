import os
import random
import sys
from ImportEngine.Ingestor import Ingestor, QuoteModel, FileExtensionNotSupported
from memeEngine.memeEngine import MemeEngine, PathNotFound


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            try:
                quotes.extend(Ingestor.parse(f))
            except FileExtensionNotSupported as e:
                print(e)
                sys.exit(1)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./')
    try:
        path = meme.make_meme(img, quote.body, quote.author)
    except PathNotFound as e:
        print(e)
        sys.exit(1)

    return path

