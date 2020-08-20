import nltk
import os
from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize,word_tokenize 
from gensim import corpora, models, similarities
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
from gensim.similarities.docsim import Similarity
import pandas as pd

"""
Question 1

Write a function that takes the file name ofa page with a list of musicians as an input, 
and returns a list of URLs that point to articles on each musician in the list.

Example of use: get_musicians("boogiewoogie.html")
The output should be a list of strings:

['https://en.wikipedia.org/wiki/Rob_Agerbeek',
 'https://en.wikipedia.org/wiki/Albert_Ammons',
 'https://en.wikipedia.org/wiki/Andrews_Sisters',
 'https://en.wikipedia.org/wiki/Winifred_Atwell',
 'https://en.wikipedia.org/wiki/Bob_Baldori',
 ...]
"""
def get_musicians(filename):
    import codecs
    from bs4 import BeautifulSoup
    f = codecs.open(filename, 'r', 'utf-8')
    soup = BeautifulSoup(f.read(),'lxml')
    #
    # Question 1
    #

    
"""
Question 2


Write a function that scrapes the text on a musician’s page and returns it as a text 
string. The input is the name of the file that contains the musician's page.

Example of use: get_text('carolinedahl.html')
should output the text of the page.
"""
def get_text(file):
    import codecs
    from bs4 import BeautifulSoup
    f = codecs.open(file, 'r', 'utf-8')
    #
    # Question 2
    #

"""
Question 3

Use the Learning Sample in the samples folder to construct an LSI model. 
Then, use the LSI model to find the most similar musician from the learning sample 
(folder 'samples') for each musician in the test sample (folder 'test'). Then, save in a CSV
the name of a musician from the test sample, and the name of the most similar musician 
from the learning sample.

Example of output (don't forget the header):

TestName,SampleName
MelvinSparks,HenryGraymusician
RooseveltSykes,RooseveltSykes
BillyEckstine,FatsDomino
JimmyWitherspoon,MoonMullican
"""
def run():
    #
    # Question 3
    # 
    # This function can be quite long!
    #
    # Hint: You should create a dataframe df with two columns,
    # TestName, SampleName
    # then dump this dataframe in a csv with the code:
    # 
    # df.to_csv('output.csv',index=False)
    