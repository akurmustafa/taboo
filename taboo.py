
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
        self.word = word
        if len(forbidden) != 5:
            raise ValueError('Number of the taboo words should be 4')
        self.forbidden = forbidden

    def get_forbidden(self):
        return self.forbidden

    def get_word(self):
        return self.word

    def add_to_database(self):
        database = load_database()
        if self.word not in [data[0] for data in database]:
            database.append([self.word] + self.forbidden)
            update_database(database)
        else:
            print('Word is already in the database')


def update_database(database):
    with open('database.txt', 'w', encoding='utf-8') as file:
        for item in database:
            for word in item:
                print(word)
                file.write(word)
                if word != item[-1]:
                    file.write(', ')
            if item != database[-1]:
                file.write('\n')


def load_database():
    database = codecs.open('database_turkish.txt', 'r', encoding='utf-8').readlines()
    database = [cur_line.strip() for cur_line in database]
    database = [cur_line.split(', ') for cur_line in database]
    return database


def delete_from_database(word):
    database = load_database()
    if word not in [data[0] for data in database]:
        # add the database remove part
        pass
    else:
        print('The', word, 'is not in the database already')


def play_current_turn(time_permitted=5):
    count = 0
    database = load_database()
    team_A_score = 0
    team_B_Score = 0
    rand_place = math.floor(random.random()*len(database))
    # print(rand_place)
    cur_word = database[rand_place][0]
    print('The word you will describe is', cur_word)
    print('Taboo words are', database[rand_place][1:])
    for i in range(time_permitted+1):
        print('Remaining time is ', str(time_permitted-i), 'seconds')
        time.sleep(1)   # waits for 1 second
    print('Time is finished')
    return cur_word


def check_data_base():
    database = load_database()
    error = 0
    for i in database:
        if len(i) != 6:
            error += 1
    return error


# tabu = Taboo('ben', ['çatı', 'ereğli', 'balkon', 'bahçe'])
# tabu.add_to_database()

# timePermitted = 10  #seconds
# play_game(time_permitted)
