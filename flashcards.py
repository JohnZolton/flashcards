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

flashcard = ('Front of card', 'Back of card')
frontcard = flashcard[0]
backcard = flashcard[1]

def showanswer():
    lbl_display['text'] = backcard
    showans.pack_forget()

window = Tk()
window.title('Scanki')
window.columnconfigure(0, minsize=500)
window.rowconfigure([0,1], minsize=100)

frame1 = Frame(window, padding='3 3 12 12')
frame2= Frame(borderwidth=1)

frame1.grid(padx= 5, pady= 5, row=0, column= 0)
frame2.grid(row=1, column=0, sticky='s')

lbl_display = Label(master=frame1, text = frontcard)
lbl_display.pack()

showans = Button(master=frame2, text= "Show Answer", command=showanswer)
showans.pack()




"""hard = Button(text = "Hard", foreground='red')
medium = Button(text = "Medium", foreground='orange')
easy = Button(text ="Easy", foreground='green')"""

window.mainloop()