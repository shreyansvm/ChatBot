#!/usr/bin/env python
# -*- coding: utf- 8 -*-
from __future__ import print_function, unicode_literals
import random
import logging
import os

import time


os.environ['NLTK_DATA'] = os.getcwd() + '/nltk_data'

from textblob import TextBlob
from flask import Flask
# # not working
# from config import FILTER_WORDS
import config

# TODO : Assign user an avatar and call it by that name
AVATAR = ["WHALE", "EARTHWORM", "ELEPHANT"]
# Default user avatar
user_avatar = ""
AVATAR_USER_RESPONSE = ["nah", "no", "no way!", "Bye", "that's rude"]

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "howdy", "how are you", "how")
GREETING_RESPONSES = ["'sup bro", "hey", "Hola Amigo!", "howdy", "watcha doing?"]
GREETING_RECEIVED = 0
GREETING_EXCHANGED = 0
### cocoBot initiates bye
COCO_INIT_BYE = ["Hey buddy, gotta go.", "Sorry to interrupt, but I need to go", "my abuela calling, gotta go!"]
# user says something
COCO_FINAL_BYE = ["Ok bye!", "cya", "astalavista!", "bye", "you bet!"]

### user initiates bye
USER_INIT_BYE = ["Ok bye!", "cya", "astalavista!", "bye"]
# cocoBot says something
USER_INIT_BYE_COCO_RESP = ["Coolio, take care.", "bye", "astalavista!", "Cya", "you bet!"]

def cocoResponds(message):
    global GREETING_RECEIVED, GREETING_EXCHANGED
    msg = TextBlob(message)
    for word in msg.words:
        if GREETING_RECEIVED == 0:
            if word.lower() in GREETING_KEYWORDS:
                GREETING_RECEIVED = 1
                #return random.choice(GREETING_RESPONSES)
                print("Coco >> ", random.choice(GREETING_RESPONSES))
                GREETING_EXCHANGED = 1

def findIfUserLikesTheAvatar(avatarUserResp):
    userHappyForAvatar = 1
    avatarUserRespMsg = TextBlob(avatarUserResp)
    for word in avatarUserRespMsg.words:
        if word.lower() in AVATAR_USER_RESPONSE:
            return 0

    return userHappyForAvatar

'''
CocoBot assigns a random avatar to the user
'''
def cocoAssignsAvatar():
    global user_avatar
    avatar = random.choice(AVATAR)
    print("Coco >> I love ", avatar, ". Can I call you - ", avatar, "?")
    avatarUserResp = raw_input(str(user_avatar) + " >> ")

    while findIfUserLikesTheAvatar(avatarUserResp) == 0:
        AVATAR.remove(avatar)
        # TODO : How will you handle 'IndexError: list index out of range' when all avatars from AVATAR are popped
        avatar = random.choice(AVATAR)
        print("Coco >> How about ", avatar, "?")
        avatarUserResp = raw_input(str(user_avatar) + " >> ")

'''
If User or CocoBot wishes to end the chat
'''
def cocoWantsABreak(type):
    if type == "cocoInitBye":
        print("Coco >> ", random.choice(COCO_INIT_BYE))
    elif type == "cocoFinalBye":
        print("Coco >> ", random.choice(COCO_FINAL_BYE))
    elif type == "userInitCocoFinalBye":
        print("Coco >> ", random.choice(USER_INIT_BYE_COCO_RESP))


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

    # TODO : how can you keep the bot alive for infinite duration OR until the user enters some keyword like 'Bye'
    while 1:
        if initialGreetings == 0:
            cocoBot(welcome)
            # TODO : calling here also doesn't work.
            # cocoAssignsAvatar()
        else:
            cocoBot(response)
        initialGreetings = 1

        response = raw_input()
        responseMsg = TextBlob(response)
        # TODO : calling here is not working
        cocoAssignsAvatar()

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