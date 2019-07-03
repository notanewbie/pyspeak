# -*- coding: cp1252 -*-
import random
import math
import time
import sys
import os
from findtext import scour
import urllib2
from  pyspeak import Speak
from parse import parseChars
from parse import harshChars
try:
    tempfile = open("settings.pts", "r");
    settings = file.read(tempfile);
    tempfile.close();
except IOError:
    tempfile = open("settings.pts", "w");
    tempfile.write("botname = BRIAN\nupdate = yes")
    tempfile.close();
    tempfile = open("settings.pts", "r");
    settings = file.read(tempfile);
    tempfile.close();
c = 0
while c < len(settings.split("\n")):
    try:
        if settings.split("\n")[c].split(" = ")[0] in "botname":
            botname = settings.split("\n")[c].split(" = ")[1]
        if settings.split("\n")[c].split(" = ")[0] in "autoupdate":
            update = settings.split("\n")[c].split(" = ")[1]
        if settings.split("\n")[c].split(" = ")[0] in "tts":
            tts = settings.split("\n")[c].split(" = ")[1]
        if settings.split("\n")[c].split(" = ")[0] in "static":
            static = settings.split("\n")[c].split(" = ")[1]
    except IndexError:
        c = c + 1
    c = c + 1
st = ""
try:
    botname
    st = st + "botname = " + botname + "\n"
except NameError:
    botname = "BRIAN"
    st = st + "botname = BRIAN\n"
try:
    tts
    st = st + "tts = " + tts + "\n"
except NameError:
    tts = "on"
    st = st + "tts = on\n"
try:
    static
    st = st + "static = no\n"
except NameError:
    update = "yes"
    st = st + "static = yes\n"
#print st
#print botname
#print update
#print tts
tempfile = open("settings.pts", "w");
tempfile.write(st)
tempfile.close();
#This is BRIAN, a Bot Really Intelligent And Nice.
#
#
#This code is still undergoing Beta testing.

#Function to parse harmful characters.
#Make a new function. This will be the engine.
def BRIAN(user, r=""):
    #Look in the database for a match to "User" so I can respond.
    #Do I know how to respond?
    INPUT = parseChars(user)
    try:
        RESPO = parseChars(r)
    except AttributeError:
        RESPO = "";
    try:
        DBup = open("DB/" + INPUT + ".ph", "w");
        DBup.write(user);
        file.close(DBup);
        PHup = open("PH/" + RESPO + ".ph", "w");
        PHup.write(user);
        file.close(PHup);
    except NameError:
        DBup = open("DB/" + INPUT + ".ph", "w");
        DBup.write(user);
        file.close(DBup);
        PHup = open("PH/" + RESPO + ".ph", "w");
        PHup.write(user);
        file.close(PHup);
    USER = parseChars(user)
    exists = os.path.isfile("PH/" + USER + ".ph");
    #If I do
    if exists is True:
        #Load the entry
        Respo = open("PH/" + USER + ".ph", "r");
        respo = file.read(Respo);
        Respo.close();
        #reply
        if "off" in tts:
            exists = exists
        else:
            Speak(respo)
        print botname + ": " + respo + "\nYOU: ";
        return respo;
        
    #If I don't
    if exists is False:
        #Choose a similar response:
        PHDB = os.listdir("PH/");
        T = open("PH/" + scour(user, PHDB)[0], "r");
        respo = file.read(T);
        T.close();
        if "off" in tts:
            exists = exists
        else:
            Speak(respo)
        print botname + ": " + respo;
        return respo;
#DEMO CODE:
#
#Speak("I'm eighteen years old but I'm not done yet. I'm not Molly and I'm not Percocet.")

#BRIAN(raw_input("YOU: "))

'''
 ____________________
|  ________________  |
| |________________| |
|                    |
|  ________________  |
| |                | |
| |   __________   | |
| |  |          |  | |
| |__|          |__| |
|____________________|

notanewbie made this.

'''
