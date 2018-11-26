# taboo game project
import codecs
import unicodedata
import numpy as np
import random
import time
import math
from tkinter import *
from tkinter import ttk

class Taboo(object):
    def __init__(self, word, forbidden):
        self.word=word
        if len(forbidden)!=5:
            raise ValueError('Number of the taboo words should be 4')
        self.forbidden=forbidden

    def getForbidden(self):
        return self.forbidden

    def getWord(self):
        return self.word

    def addToDatabase(self):
        database = loadDatabase()
        if self.word not in [data[0] for data in database]:
            database.append([self.word] + self.forbidden)
            updateDatabase(database)
        else:
            print('Word is already in the database')

def updateDatabase(database):
    with open('database.txt', 'w', encoding='utf-8') as file:
        for item in database:
            for word in item:
                print(word)
                file.write(word)
                if word != item[-1]:
                    file.write(', ')
            if item != database[-1]:
                file.write('\n')

def loadDatabase():
    database = codecs.open('databaseTurkish.txt', 'r', encoding='utf-8').readlines()
    database = [curline.strip() for curline in database]
    database = [curline.split(', ') for curline in database]
    return database

def deleteFromDatabase(word):
    database = loadDatabase()
    if word not in [data[0] for data in database]:
        # add the database remove part
        pass
    else:
        print('The', word, 'is not in the database already')

def playCurrentTurn(timePermitted=5):
    count=0
    database = loadDatabase()
    teamAScore=0;
    teamBScore=0;
    randPlace = math.floor(random.random()*len(database))
    # print(randPlace)
    curWord =database[randPlace][0]
    print('The word you will describe is', curWord)
    print('Taboo words are', database[randPlace][1:]) 
    for i in range(timePermitted+1):
        print('Remaining time is ', str(timePermitted-i),'seconds')
        time.sleep(1)   # waits for 1 second
    print('Time is finished')
    return curWord

# tabu=Taboo('ben', ['çatı', 'ereğli', 'balkon', 'bahçe'])
# tabu.addToDatabase()

# timePermitted=10    #seconds
# playGame(timePermitted)
