from flask import Flask 
from histogram import histogram
from sample import random_word
import os


app = Flask(__name__)

@app.route('/')
def generate_words():
    my_file = open("./tintern_abbey.txt", "r")
    lines =  my_file.readlines()
    my_histogram = histogram(lines)
    
    word = random_word(my_histogram)
    return word

if __name__ == '__main__':
    app.run(debug=True)