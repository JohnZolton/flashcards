from tkinter import *
from tkinter.ttk import *
import random
import time

# exported anki deck is "{front}     {back}       {number}"
# read cards from text file into list of cards
flashcards = []
with open('Spanish Vocabulary Top 5000 2.txt') as f:
    for row in f:
        card = row.split("		") # anki decks are tab delineated
        if len(card) != 3: 
            continue # skip non-compliant cards
        flashcards.append(card)

# select X cards to study
curr_deck = 10
cards = random.sample(flashcards, curr_deck)

# TODO have user select deck from GUI
# TODO set deck size
# TODO edit card
# TODO save progress / studied cards
# TODO play a scary noise + picture randomly
# TODO make it dark mode // prettier

flashcard = random.choice(cards)

def pause():
    if random.randint(1,100) < 15:
        showans.pack_forget()
        lbl_display['text'] = "rest"
        lbl_display.after(6000, showfront)

def showfront():
    lbl_display['text'] = flashcard[0]
    showans.pack()


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
    global flashcard
    cards.remove(flashcard) # card was easy so remove from pile
    flashcard = random.choice(cards)
    lbl_display['text'] = flashcard[0]
    hidebuttons()
    bar()
    pause()


def logmedium():
    #TODO update card rating // time to see again
    # move to next card
    global flashcard
    flashcard = random.choice(cards)
    lbl_display['text'] = flashcard[0]
    hidebuttons()
    pause()



def loghard():
    #TODO update card rating // time to see again
    # move to next card
    global flashcard
    flashcard = random.choice(cards)
    lbl_display['text'] = flashcard[0]
    hidebuttons()
    pause()


window = Tk()
window.title('Scanki')
window.columnconfigure(0, minsize=500)
window.rowconfigure([0,1], minsize=50)

frame1 = Frame(window)
frame2= Frame(window, borderwidth=1)

frame0 = Frame(window, height= 10)
frame0.grid(row = 0, column = 0, sticky='N')
frame1.grid(row=1, column= 0)

frame2.grid(row=2, column=0, sticky='s', pady=10)

# implemented a progress bar
bar_progress = Progressbar(frame0, orient = HORIZONTAL,
        length = 100, mode = 'determinate')
def bar():
    global cards
    bar_progress['value'] = 100*(curr_deck - len(cards))/curr_deck
bar_progress.pack(pady=10)

# main display, alternates between frontcard, backcard, and 'rest'
lbl_display = Label(master=frame1, text = flashcard[0])
lbl_display.pack()

# button to show the answer
showans = Button(master=frame2, text= "Show Answer", command=showanswer)
showans.pack()

# buttons to move on to the next card
btn_hard = Button(master=frame2, text = "Hard", command=loghard)
btn_medium = Button(master=frame2, text = "Medium", command=logmedium)
btn_easy = Button(master=frame2, text ="Easy", command=logeasy)



window.mainloop()