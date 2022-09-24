from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.ttk import *
import random
from PIL import Image, ImageTk
import datetime



def pause():
    # random scary picture, for adrenaline boost to improve memory
    if random.randint(1,100) < 14:
        img = ImageTk.PhotoImage(file = 'Ghost_Emoji.png')

        lbl_display.configure(image=img)
        lbl_display.image=img
        
        lbl_display.after(2000, removepic)
    # random pause
    if random.randint(1,100) < 15:
        showans.pack_forget()
        lbl_display['text'] = "rest"
        lbl_display.after(6000, showfront)

def removepic():
    lbl_display.configure(image='')
        
    
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
    # remove card and move to next card
    global flashcard
    flashcard[2] = datetime.date.today() + datetime.timedelta(days=3) # set due date to 3 days from now
    if len(cards) >= 2:
        cards.remove(flashcard) # card was easy so remove from pile
        flashcard = random.choice(cards)
        lbl_display['text'] = flashcard[0]
        hidebuttons()
        bar()
        pause()
    else:
        lbl_display['text'] = "CONGRATULATIONS, STUDY COMPLETED"
        hidebuttons()
        showans.pack_forget()
        bar_progress['value'] = 100



def logmedium():
    # move to next card 
    global flashcard
    flashcard[2] = 2 # type 2 cards are seen and need to be seen again
    flashcard = random.choice(cards)
    lbl_display['text'] = flashcard[0]
    hidebuttons()
    pause()


def loghard():
    # move to next card
    global flashcard
    flashcard[2] = 1 # type 1 cards have been seen and need to be seen again
    flashcard = random.choice(cards)
    lbl_display['text'] = flashcard[0]
    hidebuttons()
    pause()

def edit():
    global flashcard
    new_front = simpledialog.askstring("Front", "New Front Card")
    new_back = simpledialog.askstring("Back", "New Back Card")
    if new_front:
        flashcard[0] = new_front
    if new_back:
        flashcard[1] = new_back


# exported anki deck is "{front}     {back}       {number}"
# read cards from text file into list of cards
flashcards = []
# select deck from files
path = filedialog.askopenfilename(initialdir='C:\\Users\\jgz6\\Documents\\Coding', title = 'Select File')
with open(path) as f:
    for row in f:
        card = row.split("		") # anki decks are tab delineated
        if len(card) < 3: 
            continue # skip non-compliant cards
        if len(card) == 3:
            card.append(datetime.date.today()+datetime.timedelta(days=365)) # initialize due date to far in the future
        flashcards.append(card)
        # list of [front, back, count, date due]

# select X cards to study
# pick due cards first
curr_deck = int(simpledialog.askfloat('Cards to study', 'Cards to study'))
# sort by date due
flashcards.sort(key=lambda x:x[3])
cards = flashcards[0:curr_deck]
flashcard = random.choice(cards)
card_dist = round(curr_deck/3)

# TODO save progress / studied cards





window = Tk()

window.title('Anki Clone')
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
bar_progress.grid(row = 0, column=2, sticky=E, padx=100, pady=10)

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

# edit button to edit front/back of card
btn_edit = Button(master= frame0, text= "Edit", command=edit)
btn_edit.grid(row= 0, column=0, sticky= W, padx=100, pady=10)

window.mainloop()