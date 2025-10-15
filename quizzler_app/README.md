# 🧠 Quizler – Trivia Game

A fun and interactive **Trivia Game** built with **Python** and **Tkinter**, fetching questions dynamically from the [Open Trivia Database](https://opentdb.com/). Test your knowledge with True/False questions and see how many you can get right!

---

## 🚀 Features

* Fetches **True/False trivia questions** from an online API.
* Tracks **score in real-time**.
* Immediate **feedback with color changes** (green for correct, red for wrong).
* **Clean and simple GUI** built with Tkinter.
* Fully modular code for easy extension.

---

## 🛠️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/quizler.git
```

2. **Navigate to the project folder**:

```bash
cd quizler
```

3. **Install required packages**:

```bash
pip install requests
```

4. **Run the game**:

```bash
python main.py
```

> Make sure you have the `images/true.png` and `images/false.png` files in the `images` folder.

---

## 🧩 Project Structure

```
quizler/
│
├── main.py          # Entry point of the game
├── data.py          # Fetches questions from Open Trivia DB
├── question_model.py # Question class
├── quiz_brain.py    # Quiz logic and scoring
├── ui.py            # Tkinter GUI
└── images/          # True/False button images
```

---

## ⚡ Usage

* Click **True** or **False** to answer each question.
* The **background will turn green** for correct answers, **red** for wrong answers.
* Your score updates immediately after each question.
* At the end, the quiz displays a completion message.

---

## 💡 Future Improvements

* Add support for **multiple-choice questions**.
* Show **categories and difficulty levels**.
* Include a **restart quiz** option.
* Save **high scores** locally.

---

## 📄 License

This project is **open-source** and free to use for learning and personal projects.
