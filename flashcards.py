"""
This is a flashcard app, inspired by anki and Dr. Andrew Huberman

GUI: 
    Stage 1: show answer
    Stage 2: rate answer easy/medium/hard
        click/keystroke -> next card
    Stage 3: edit card - front/back
             delete card

cards:
    front
    back
    spaced repetition marker 
    * would be cool if you could import anki decks

random scary sound + picture
    shown at random after you click "next card"

90-minute timer? display/hide

semi-random 10 second breaks

* Release of adrenaline tells your neurons to remember the events directly
before the release of adrenaline, flashing a scary image + sound may
startle you and release some adrenaline, helping you remember what you
are studying. Maybe later I'll wire this up to a shock collar.
"""

from tkinter import *
from tkinter.ttk import *
import random

# exported anki deck is {front} {back} {number}
# read cards from text file into list of cards
flashcards = []
with open('Spanish Vocabulary Top 5000 2.txt') as f:
    for row in f:
        card = row.split("		") # anki decks are tab delineated
        if len(card) != 3: continue
        flashcards.append(card)
flashcards.sort(key= lambda x:int(x[2]))

# select 10 cards
cards = random.sample(flashcards, 10)


# TODO save progress / studied cards

flashcard = random.choice(cards)

def showanswer():
    lbl_display['text'] = flashcard[1]
    showans.pack_forget()
    btn_easy.pack(side=LEFT)
    btn_hard.pack(side=RIGHT)
    btn_medium.pack(side=RIGHT)
    
def hidebuttons():
    btn_easy.pack_forget()
    btn_medium.pack_forget()
    btn_hard.pack_forget()
    showans.pack()

def logeasy():
    # update card rating // time to see again
    # move to next card
    cards.remove(flashcard)
    lbl_display['text'] = flashcard[0]
    hidebuttons()

def logmedium():
    #TODO update card rating // time to see again
    # move to next card
    lbl_display['text'] = flashcard[0]
    hidebuttons()

def loghard():
    # update card rating // time to see again
    # move to next card
    lbl_display['text'] = flashcard[0]
    hidebuttons()

window = Tk()
window.title('Scanki')
window.columnconfigure(0, minsize=500)
window.rowconfigure([0,1], minsize=100)

frame1 = Frame(window, padding='3 3 12 12')
frame2= Frame(borderwidth=1)

frame1.grid(padx= 5, pady= 5, row=0, column= 0)
frame2.grid(row=1, column=0, sticky='s')

lbl_display = Label(master=frame1, text = flashcard[0])
lbl_display.pack()

showans = Button(master=frame2, text= "Show Answer", command=showanswer)
showans.pack()


btn_hard = Button(master=frame2, text = "Hard", command=loghard)
btn_medium = Button(master=frame2, text = "Medium", command=logmedium)
btn_easy = Button(master=frame2, text ="Easy", command=logeasy)

window.mainloop()