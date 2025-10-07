# NATO Phonetic Alphabet Converter 🔡➡️🔤

A small Python program that converts any word into the **NATO phonetic alphabet**.  
For example, `MARCO` becomes: `['Mike', 'Alfa', 'Romeo', 'Charlie', 'Oscar']`.

---

## 📂 How it works
- Reads the NATO alphabet data from `nato_phonetic_alphabet.csv` using **pandas**.  
- Creates a dictionary mapping each letter to its phonetic code.  
- Uses a `while True` loop with error handling (`try/except`) to keep asking until the user enters valid input.  

---

## ▶️ How to run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/nato-phonetic-alphabet.git
   cd nato-phonetic-alphabet
2. Make sure you have Python 3 and pandas installed:
    ```bash
    pip install pandas

3. Run the script:
    ```bash
    python main.py

## 📌 Example

    Enter a name: Marco
    ['Mike', 'Alfa', 'Romeo', 'Charlie', 'Oscar']

If you enter an invalid character (like a number or symbol):
    
    Enter a name: M4RCO
    ❌ Invalid input. Please enter only alphabet letters.
Then it will ask again until valid input is entered.


## ✨ Notes

- Only works with letters (A–Z).

- Great for practicing **pandas**, **dictionary comprehension**, **list comprehension**, and **error handling** with `try`/`except`.
- Simple and beginner-friendly project.
