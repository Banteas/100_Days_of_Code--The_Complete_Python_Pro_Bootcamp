# 🐢 Turtle Crossing Game

A fun arcade-style game built with Python's `turtle` module.  
Guide the turtle safely across the road while avoiding cars.  
Each time you reach the finish line, the game gets harder! 🚗💨

---

## ✨ Features
- 🎮 **Player controls**: move the turtle up and down with the arrow keys.  
- 🚗 **Random cars**: cars spawn at random lanes and colors.  
- ⏩ **Difficulty increase**: car speed increases every time you level up.  
- 🏆 **Scoreboard**: track your level at the top left.  
- 💀 **Collision detection**: game over when you hit a car.

---

## 🎹 Controls
- ⬆️ **Up Arrow** → Move turtle up  
- ⬇️ **Down Arrow** → Move turtle down  

---

## ▶️ How to Run
```bash
# clone the repo
git clone https://github.com/your-username/turtle-crossing-game.git
cd turtle-crossing-game

# run the game
python main.py
```
📂 Project Structure

    turtle-crossing-game/
    │
    ├── main.py          # game loop & event handling
    ├── player.py        # player (turtle) logic
    ├── car_manager.py   # car creation & movement
    ├── scoreboard.py    # scoreboard & game over text
    └── README.md        # project description
🚀 Future Ideas

- Add left/right movement for the player.

- Introduce multiple lanes with different car speeds.

- Keep track of high scores across sessions.

- Add background music or sound effects.
