#/usr/bin/python
##exercise 41
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORD = []

PHRASES = {
		"class ###(###):": "Make a class named ### that is-a ###.",
		"class ###(object): \n\tdef __init__(self,***)" : "class ### has-a __init__ that takes self and *** parameters.",
		"class ###(object): \n\tdef ***(self, @@@)": "class ### has-a function named *** that takes self and @@@ parameters."
		"*** = ###()": "Set *** to an instance of class ###.",
		"***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
		"***.*** = '***'": "From *** get the *** attribute and set it to '***'."
		}


