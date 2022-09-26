# flashcards

This is a flashcard app, inspired by Anki and Dr. Andrew Huberman, created using Tkinter. 

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
 
 ![image](https://user-images.githubusercontent.com/102374100/192285116-93886d4f-d149-4c51-9b63-ff4cc527514e.png)

![image](https://user-images.githubusercontent.com/102374100/192285337-d7023b49-5c38-467a-a868-15e62e5d3639.png)

![image](https://user-images.githubusercontent.com/102374100/192285434-e74e9aa1-2874-455c-acdc-89d2b43cfc39.png)

Randomly flash a scary picture to boost adrenaline:![image](https://user-images.githubusercontent.com/102374100/192296505-cad7d881-f884-4206-b044-de2752155aae.png)


![image](https://user-images.githubusercontent.com/102374100/192285689-afa4d222-eb32-4ef6-9c87-7197573ae922.png)

![image](https://user-images.githubusercontent.com/102374100/192294097-50fa4d8e-272a-437e-a5dc-ed64dac002ec.png)
