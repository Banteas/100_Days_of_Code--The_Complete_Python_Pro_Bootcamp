import random
from tkinter import *
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- READ DATA ------------------------------- #
# Try to load words the user still needs to learn.
# If that file doesn't exist yet (first run), load the original full list instead.
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    french_list = original_data.to_dict(orient='records')
else:
    french_list = data.to_dict(orient='records')  # List of dictionaries

# ---------------------------- CREATE NEW FRENCH CARD ------------------------------- #
def next_card():
    """Picks a random French word and displays it on the front of the flash card."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel any existing flip timer

    current_card = random.choice(french_list)  # Choose a random card (dict)
    french = current_card["French"]

    # Update canvas to show the French word
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french, fill="black")

    # Schedule the card to flip after 3 seconds
    flip_timer = window.after(3000, flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    """Flips the card to show the English translation."""
    english = current_card['English']

    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english, fill="white")

# ---------------------------- MARK WORD AS KNOWN ------------------------------- #
def known_word():
    """
    Removes the current card from the list (the user knows it),
    saves progress to a CSV file, and shows the next card.
    """
    global current_card

    # Remove the known word from the list
    french_list.remove(current_card)

    # Save the updated list so progress is kept even after closing
    new_data = pd.DataFrame(french_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    # Show the next word
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Create the timer (it will later be cancelled and restarted each time)
flip_timer = window.after(3000, flip_card)

# Setup the flashcard canvas
canvas = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons for "I don't know" and "I know"
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

unknown_button = Button(window, image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_button = Button(window, image=right_img, highlightthickness=0, command=known_word)
known_button.grid(column=1, row=1)

# Start the program by showing the first card
next_card()

window.mainloop()
