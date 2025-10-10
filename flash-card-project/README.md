# 🧠 Flashy - French Flash Cards

A simple flash card app built with **Python** and **Tkinter**.

It helps you practice French words by showing one side in French and flipping to English after a few seconds.

---

## 🚀 Features
- Randomly shows French words
- Automatically flips to English after 3 seconds
- Save your progress — known words are removed from the list
- Next time you open the app, it continues where you left off

---

## 🖼️ How it Works
When you know a word, click ✅ and it will disappear from the list.  
If you don’t, click ❌ and you’ll see another card.  
Your progress is saved automatically in `data/words_to_learn.csv`.

---

## 💻 Run the App

1. Make sure you have Python installed  
2. Install `pandas`:
   ```bash
   pip install pandas
3. Run the app:
    ```bash
   python main.py
   
## 🗂️ File Structure
    Flashy/
    │
    ├── main.py
    ├── data/
    │   ├── french_words.csv
    │   └── words_to_learn.csv
    ├── images/
    │   ├── card_front.png
    │   ├── card_back.png
    │   ├── right.png
    │   └── wrong.png
    └── README.md

## 🧠 What I Learned

How to use Tkinter for GUI apps

How to handle CSV files with Pandas

How to use try / except for file handling

How to save progress and update data dynamically