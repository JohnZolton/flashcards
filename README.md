# flashcards

This is a flashcard app, inspired by Anki and Dr. Andrew Huberman, created using Tkinter. 

During a study session, random short rest intervals boost learning speed. The neurons activated while studying actually fire faster during this rest interval resulting in stronger memory formation. Additionally, an adrenaline spike signals the brain to remember the events directly before the adrenalien jump. Like when people experience a traumatic event can vividly remember many details. We can take advantage of these biological mechanisms to study more effectively! My favorite memorization tool is Anki, unfortunately it lacked any features to capitalize on these two mechanisms, so I built my own from scratch using Tkinter. Its key features include random rest intervals and randomly flashing a scary picture to boost adrenaline.  

Key Features:
 - Random rest intervals after a completed card. This boosts memory and learning speed. [Overview](https://www.auxoro.com/blog/learn-skills-faster-andrew-hubereman-neuroscience), [Study](https://www.sciencedirect.com/science/article/pii/S2211124721005398).
 - Randomly flashes a scary picture. This causes an adrenaline jump which signals the brain to remember the events immediately before. [Source](https://www.youtube.com/watch?v=JPX8g8ibKFc&t=3422s). 
 
Features:
 - Select a deck of flashcards to use (as a CSV)
 - Set # of cards desired to study
 - Sorts cards by due date, displays front of card, and progress bar representing completed cards, and allows editing the front and back of the current card
 - Once answer is shown, rate the card as easy, medium or hard and the next card is displayed
   - Easys are removed from the pile and the progress bar updates
   - Mediums will be shown again after 5 cards
   - Hards will be shown again after 3 cards
 - Bound keys to buttons for ease of use (ex: spacebar = next)
 - Cards are tracked using due dates, cards without due dates are assigned as due today. Once a card is marked 'easy' its due date is updated to three days from now. The CSV is sorted according to due date so the earliest "due" cards are selected.
 - Saves progress upon closing the window by writing the updated flashcard deck to the original CSV file
 
 Anki decks can be exported as a tab deliminated text file. Converter.py converts this file to CSV format. 
 
 ![image](https://user-images.githubusercontent.com/102374100/192285116-93886d4f-d149-4c51-9b63-ff4cc527514e.png)

![image](https://user-images.githubusercontent.com/102374100/192285337-d7023b49-5c38-467a-a868-15e62e5d3639.png)

![image](https://user-images.githubusercontent.com/102374100/192285434-e74e9aa1-2874-455c-acdc-89d2b43cfc39.png)

Randomly flash a scary picture to boost adrenaline:![image](https://user-images.githubusercontent.com/102374100/192296505-cad7d881-f884-4206-b044-de2752155aae.png)


![image](https://user-images.githubusercontent.com/102374100/192285689-afa4d222-eb32-4ef6-9c87-7197573ae922.png)

![image](https://user-images.githubusercontent.com/102374100/192294097-50fa4d8e-272a-437e-a5dc-ed64dac002ec.png)
