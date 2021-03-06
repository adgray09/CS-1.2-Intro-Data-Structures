from histogram import histogram
from sample import random_word
from read_file import read_file
from markov import MarkovChain

def generate_sentence():
    my_file = read_file("tintern_abbey.txt")
    my_histogram = histogram(my_file.split("\n"))
    
    sentence = ""
    num_words = 10
    for i in range(num_words):
        word = random_word(my_histogram)
        sentence += " " + word
    return sentence