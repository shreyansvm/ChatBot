#!/usr/bin/env python
# -*- coding: utf- 8 -*-
from __future__ import print_function, unicode_literals
import random
import logging
import os

import sys
print(sys.executable)

os.environ['NLTK_DATA'] = os.getcwd() + '/nltk_data'

from textblob import TextBlob
from flask import Flask
# # not working
# from config import FILTER_WORDS
import config

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "howdy", "how are you", "how")
GREETING_RESPONSES = ["'sup bro", "hey", "Hola Amigo!"]

def byteResponds(message):
    msg = TextBlob(message)
    for word in msg.words:
        if word.lower() in GREETING_KEYWORDS:
            #return random.choice(GREETING_RESPONSES)
            print(random.choice(GREETING_RESPONSES))


def byteBot(message):
    print(message)
    byteResponds(message)

# checking if we are running in the main scope
if __name__ == "__main__":
    import sys

    # Take the input string passed while starting the program
    # python myBot.py "Hi Byte"
    if (len(sys.argv) > 1):
        welcome = sys.argv[1]
    else:
        welcome = "How are you, Byte?"
    # TODO : how can you keep the bot alive for infinite duration OR until the user enters some keyword like 'Bye'
    byteBot(welcome)

