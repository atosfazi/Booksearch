# Booksearch
Django based web app for searching similar book positions to the given title. The search engine is based on book embedding space.The database consists of almost six thousand polish books.

## Table of contents
* [Usage](#usage)
* [Keras model](#keras_model)
* [Requirements](#requirements)
* [Setup](#setup)

## Usage
On the main page there's a text field for entering the title or the author of the book. 

![Main page view](./images/main_page.PNG)

All similar suggestions to the entered phrase are returned. The database contains only items in Polish.

![Found books view](./images/found_books_view.PNG)

The user can display simliar positions by clicking the "Pokaż podobne" button.

![Similar books view](./images/similar_books_view.PNG)


## Keras model
Similar books are proposed based on the cosinuse similarity of their vectors obtained from embedding space. The Embedding came from the trained following model. 

![Network](./images/network.PNG)

Polish books from <a href="https://sites.google.com/eng.ucsd.edu/ucsdbookgraph">Goodreads Datasets</a> were used as learning data. 

	
## Requirements
* Python: 3.x
* Django: 3.1.3
* NumPy: 1.19.3
* Keras: 2.3.1
* TensorFlow: 2.2.0
* pandas
* Unidecode
  
## Setup
To run this project locally, open CLI in the directory with a project and run the command:

```
$ cd python manage.py runserver
```
