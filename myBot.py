#!/usr/bin/env python
# -*- coding: utf- 8 -*-
from __future__ import print_function, unicode_literals
import logging
import os , time , random
os.environ['NLTK_DATA'] = os.getcwd() + '/nltk_data'
from textblob import TextBlob
from flask import Flask
import config
from botFunctions import *
from conversationLibrary import *


def cocoBot(message):
    cocoResponds(message)

# checking if we are running in the main scope
if __name__ == "__main__":
    import sys
    initialGreetings = 0


    # Take the input string passed while starting the program
    # python myBot.py "Hi Coco"
    if (len(sys.argv) > 1):
        welcome = sys.argv[1]
    else:
        welcome = "How are you, Coco?"

    runTime = 60 ;# seconds
    startTime = time.time()

    while 1:
        if initialGreetings == 0:
            cocoBot(welcome)
        else:
            cocoBot(response)

        response = raw_input()
        chechLanguage(response)
        responseMsg = TextBlob(response)
        if initialGreetings != 1:
            cocoAssignsAvatar()
            initialGreetings = 1

        print("After cocoAssignsAvatar()")
        itsTimeForBye = 0
        for word in responseMsg.words:
            if word.lower() in USER_INIT_BYE:
                itsTimeForBye = 1

        elapsed = time.time() - startTime

        if elapsed >= runTime :
            cocoWantsABreak("cocoInitBye")
            response = raw_input(str(user_avatar) + " >> ")
            cocoWantsABreak("cocoFinalBye")
            break

        if itsTimeForBye == 1:
            cocoWantsABreak("userInitCocoFinalBye")
            break

        # TODO : if User doesn't enter for x seconds/minute, Coco should say something