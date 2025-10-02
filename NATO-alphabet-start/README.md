# NATO Phonetic Alphabet Converter 🔡➡️🔤

A small Python program that converts any word into the **NATO phonetic alphabet**.  
For example, `MARCO` becomes: `['Mike', 'Alfa', 'Romeo', 'Charlie', 'Oscar']`.

---

## 📂 How it works
- Reads the NATO alphabet data from `nato_phonetic_alphabet.csv` using **pandas**.  
- Creates a dictionary mapping each letter to its phonetic code.  
- Takes a user’s input and translates each letter.  

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

## ✨ Notes

- Only works with letters (A–Z).

- Simple beginner project to practice pandas, dict comprehension, and list comprehension.
