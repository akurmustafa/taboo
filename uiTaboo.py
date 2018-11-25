# from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, ttk
from tkinter import *
import taboo

class Taboo:

    def __init__(self, master):
        self.master = master
        master.title("Taboo Game")
        for i in range(5):
            master.grid_columnconfigure(i, minsize=100)  # set minsize for every column
            master.columnconfigure(i, weight=1)
        for i in range(5):
            master.grid_rowconfigure(i, minsize=60)  # set minsize for every row
            master.rowconfigure(i, weight=1)
        
        self.turn=False
        self.score_of_team_A = 0
        self.score_of_team_B = 0
        self.remaining_time=None
        self.current_word = None
        self.taboo_word_1 = None
        self.taboo_word_2 = None
        self.taboo_word_3 = None
        self.taboo_word_4 = None
        self.taboo_word_5 = None
        self.database = taboo.loadDatabase()

        self.score_of_team_A_label_text = IntVar()
        self.score_of_team_B_label_text = IntVar()
        self.remaining_time_label_text = StringVar()
        self.current_word_text = StringVar()
        self.taboo_word_1_text = StringVar()
        self.taboo_word_2_text = StringVar()
        self.taboo_word_3_text = StringVar()
        self.taboo_word_4_text = StringVar()
        self.taboo_word_5_text = StringVar()

        self.score_of_team_A_label_text.set(self.score_of_team_A)
        self.score_of_team_B_label_text.set(self.score_of_team_B)
        self.remaining_time_label_text.set(self.remaining_time)
        self.current_word_text.set(self.current_word)
        self.taboo_word_1_text.set(self.taboo_word_1)
        self.taboo_word_2_text.set(self.taboo_word_2)
        self.taboo_word_3_text.set(self.taboo_word_3)
        self.taboo_word_4_text.set(self.taboo_word_4)
        self.taboo_word_5_text.set(self.taboo_word_5)

        self.score_of_team_A_label = Label(master, textvariable=self.score_of_team_A_label_text)
        self.team_A_label = Label(master, text="Team A: ")
        self.score_of_team_B_label = Label(master, textvariable=self.score_of_team_B_label_text)
        self.team_B_label = Label(master, text="Team B: ")
        self.remaining_time_label = Label(master, textvariable=self.remaining_time_label_text)
        self.current_word_label = Label(master, textvariable=self.current_word_text)
        self.taboo_word_1_label = Label(master, textvariable=self.taboo_word_1_text)
        self.taboo_word_2_label = Label(master, textvariable=self.taboo_word_2_text)
        self.taboo_word_3_label = Label(master, textvariable=self.taboo_word_3_text)
        self.taboo_word_4_label = Label(master, textvariable=self.taboo_word_4_text)
        self.taboo_word_5_label = Label(master, textvariable=self.taboo_word_5_text)

        self.true_button = Button(master, text="True", command=lambda: self.update("add"))
        self.taboo_button = Button(master, text="Taboo", command=lambda: self.update("subtract"))
        self.pass_button = Button(master, text="Pass", command=lambda: self.update("Pass"))
        self.play_button = Button(master, text="Play", command=lambda: self.start_game())
        # LAYOUT
        # ROW 1
        self.team_A_label.grid(row=0, column=0, columnspan=1, sticky=(N,W,E,S))
        self.score_of_team_A_label.grid(row=0, column=1, columnspan=1, sticky=(N,W,E,S))
        self.team_B_label.grid(row=0, column=3, columnspan=1, sticky=(N,W,E,S))
        self.score_of_team_B_label.grid(row=0, column=4, columnspan=2, sticky=(N,W,E,S))

        # ROW 2
        self.current_word_label.grid(row=1, column=1, columnspan=3, sticky=(N,W,E,S))
        self.remaining_time_label.grid(row=1, column=4, columnspan=1, sticky=(N,W,E,S))
        # ROW 3
        self.taboo_word_1_label.grid(row=2, column=0, columnspan=1, sticky=(N,W,E,S))
        self.taboo_word_2_label.grid(row=2, column=1, columnspan=1, sticky=(N,W,E,S))
        self.taboo_word_3_label.grid(row=2, column=2, columnspan=1, sticky=(N,W,E,S))
        self.taboo_word_4_label.grid(row=2, column=3, columnspan=1, sticky=(N,W,E,S))
        self.taboo_word_5_label.grid(row=2, column=4, columnspan=1, sticky=(N,W,E,S))

        # ROW 4
        self.true_button.grid(row=3, column=0, columnspan=2, sticky=(N,W,E,S))
        self.taboo_button.grid(row=3, column=2, columnspan=1, sticky=(N,W,E,S))
        self.pass_button.grid(row=3, column=3, columnspan=2, sticky=(N,W,E,S))

        # ROW 5
        self.play_button.grid(row=4, column=2, columnspan=1, sticky=(N,W,E,S))

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if self.turn:
            if method == "add":
                self.score_of_team_A += 1
            elif method == "subtract":
                self.score_of_team_A -= 1
            self.score_of_team_A_label_text.set(self.score_of_team_A)
        elif not self.turn:
            if method == "add":
                self.score_of_team_B += 1
            elif method == "subtract":
                self.score_of_team_B -= 1
            self.score_of_team_B_label_text.set(self.score_of_team_B)
        self.play_current_turn()

    def play_current_turn(self): 
        randPlace = taboo.math.floor(taboo.random.random()*len(self.database))
        self.current_word = self.database[randPlace][0]
        self.taboo_word_1 = self.database[randPlace][1]
        self.taboo_word_2 = self.database[randPlace][2]
        self.taboo_word_3 = self.database[randPlace][3]
        self.taboo_word_4 = self.database[randPlace][4]
        self.taboo_word_5 = self.database[randPlace][5]

        self.current_word_text.set(self.current_word)
        self.taboo_word_1_text.set(self.taboo_word_1)
        self.taboo_word_2_text.set(self.taboo_word_2)
        self.taboo_word_3_text.set(self.taboo_word_3)
        self.taboo_word_4_text.set(self.taboo_word_4)
        self.taboo_word_5_text.set(self.taboo_word_5)
    
    def countdown(self, remaining_time = None):
        if remaining_time is not None:
            self.remaining_time = str(remaining_time)
        if int(self.remaining_time) <= 0:
            self.remaining_time ="time's up!"
        else:
            self.remaining_time = str(int(self.remaining_time) - 1)
            self.remaining_time_label_text.set(self.remaining_time)
            # self.master.after(1000, self.countdown(remaining_time=int(self.remaining_time))) 
  
    def start_game(self, time_permitted=5):
        self.turn = not self.turn
        self.database = taboo.loadDatabase()
        self.play_current_turn()
        
root = Tk()
my_gui = Taboo(root)
root.mainloop()