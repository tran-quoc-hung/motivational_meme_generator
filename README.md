# Meme Generator Overview

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.The application can be run using CLI or Web with flask:
- CLI: `python meme.py`:
  Create memes with available images and data

- Web:  `python app.py`:
  Randomly select the meme to be displayed from the images and text data available in the file.
  Create meme from url, body, author entered by user

# Instructions for setting up and running the program

- Create enviroment using requirements.txt:
  pip install -r requirements.txt
- Run CLI: `python meme.py`: 
  py meme.py --path {path} --body {body} --author {author}

- Run Web:  `python app.py`: 
  set FLASK_APP = app.py
  flask run

# Project Scaffolding

Upon starting, the project contains several files and folders to help you get up and running:

```
.
├── README.md       # This file.
├── app.py
├── meme.py
├── MemeEngine.py
├── QuoteEngine
|   |── __ini__.py
|   |── CSVIngestor.py
|   |── DocxIngestor.py
|   |── PDFIngestor.py
|   |── TXTIngestor.py
|   |── IngestorInterface.py
|   |── Ingestor.py
|   └── Quote.py
├── _data
|   |── DogQuotes
|   |── photos
|   └── SimpleLines
└──── templates
    |── base.html
    |── meme_form.html
    └── meme.html

```

Let's take a closer look at the purpose of each of these files and folders:

- `app.py`: In this file, you'll used to create web memes with flask
- `meme.py`: In this file, you'll create a Command-Line Interface tool
- `MemeEngine.py`: In this file, you'll create meme from images and data from available files 
- `QuteEngine\.`: The Quote Engine module is responsible for ingesting many types of files that contain quotes.
  - `Ingestor.py`: In this file, you'll read data from appropriate file
  - `.py`: You will read data from a file with the extension csv
  - `DocxIngestor.py`: You will read data from a file with the extension docx
  - `CSVIngestor.py`: You will read data from a file with the extension csv
  - `PDFIngestor.py`: You will read data from a file with the extension pdf
  - `TXTIngestor.py`: You will read data from a file with the extension txt
