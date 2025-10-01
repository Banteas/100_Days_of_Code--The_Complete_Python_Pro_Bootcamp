# U.S. States Game 🗺️

A fun **Python Turtle game** where you test your knowledge of U.S. states!  
Guess all 50 states correctly and see how many you know.

## Features

- Interactive map of the United States
- Type state names to reveal them on the map
- Keep track of your score with a live scoreboard
- Exit anytime to save the states you missed in `states_to_learn.csv`
- Built using Python, Turtle, and Pandas

## How to Play

1. Run `main.py` in a Python environment.
2. A window with the blank U.S. map will open.
3. Type the name of a state in the input box:
   - Correct guesses appear on the map.
   - Your score increases for each correct guess.
4. Exit the game at any time by:
   - Clicking **Cancel** on the input box
   - Typing `"Exit"` in the input box
   - Clicking the window **X** button
5. The missed states will be saved automatically in `states_to_learn.csv` for later practice.

## Requirements

- Python 3.x
- pandas (`pip install pandas`)
- Turtle (built-in with Python)

## File Structure

    ├── main.py # Game logic and main loop
    ├── state.py # State class for displaying state names on the map
    ├── scoreboard.py # Scoreboard class to track and display the score
    ├── 50_states.csv # CSV with state names and coordinates
    ├── blank_states_img.gif # Blank U.S. map image
    └── states_to_learn.csv # Generated file with missed states

## How It Works

- The game reads `50_states.csv` to get all states and their coordinates.
- The `State` class writes correct guesses on the map.
- The `Scoreboard` class tracks the score and displays it on the screen.
- If you exit, the game saves all states you didn’t guess into `states_to_learn.csv`.
