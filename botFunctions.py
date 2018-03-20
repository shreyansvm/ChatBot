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

    for word in TextBlob(avatarUserResp).words:
        if word.lower() in USER_INIT_BYE:
            cocoWantsABreak("userInitCocoFinalBye")
            exit(0)

    while findIfUserLikesTheAvatar(avatarUserResp) == 0:
        print("Inside while of cocoAssignsAvatar")
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
# Add all functions here

'''
Check user has typed in a language other than English
'''
def chechLanguage(response):
    responseMsg = TextBlob(response)
    # TODO : Needs atleast 3 characters to detect a language, otherwise it crashes with following msg
    # textblob.exceptions.TranslatorError: Must provide a string with at least 3 characters.

    # for now doing the following :
    if len(response) <= 2:
        setBaseLanguage('en')
    elif len(response) > 2:
        setBaseLanguage(responseMsg.detect_language())

'''
If user enters in some other language (not English),
    CocoBot also acts funny by starting to talk in the same language.
'''
def setBaseLanguage(lang):
    BASE_LANGUAGE = lang
    print("Global language set to - ", lang)
    print("BASE_LANGUAGE - ", BASE_LANGUAGE)
    # TODO : Do something if not in English

'''
CocoBot gets funny. Starts talking in a random language and checks if the USER knows anything
'''
def cocoBotTalksInDiffLang():
    print("Inside cocoBotTalksInDiffLang")
    # TODO : select a random language and start talking
    # TODO : get user reaction and change back to known language.

