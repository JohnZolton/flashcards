import datetime
import csv

file = "Essential Spanish Vocabulary Top 5000 test.txt"
flashcards= []
with open(file) as f:
    for row in f:
        card = row.split("		") # anki decks are tab delineated
        flashcards.append(card)
        
print(flashcards)

temp = []

receiver = "receiver.txt"
with open(receiver, 'w+', newline="") as f:
    write = csv.writer(f)
    write.writerows(flashcards)

