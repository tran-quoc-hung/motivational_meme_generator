"""Motivational meme generator app."""

import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine.Ingestor import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')
if not os.path.exists('./static'):
    os.makedirs('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # get all quote
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    # get all img
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # Use requests to save the image from the image_url
    #    form param to a temp local file.
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    try:
        r = requests.get(image_url)
        tmp = f'./{random.randint(0, 10000000)}.jpg'
        with open(tmp, 'wb') as img:
            img.write(r.content)

        # Use the meme object to generate a meme using this temp
        #    file and the body and author form paramaters.
        path = meme.make_meme(tmp, body, author)
        img.close()

        # Remove the temporary saved image.
        os.remove(tmp)
        return render_template('meme.html', path=path)
    except Exception:
        return render_template('meme.html')


if __name__ == "__main__":
    app.run()
