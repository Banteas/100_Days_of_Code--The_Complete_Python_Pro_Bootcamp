Snake Game – Day-20/21 Project

A classic Snake game built with Python’s turtle module. Control the snake to collect food, grow longer, and avoid collisions with walls or yourself.

🐍 Features

- Snake movement: Smooth movement controlled via arrow keys (Up, Down, Left, Right).

- Growing snake: Snake grows in length each time it eats food.

- Random food placement: Food appears in a random position on the screen after being eaten.

- Score tracking: A scoreboard displays the current score, which increases with every food collected.

- Collision detection: Game ends if the snake hits the walls or its own body.

- Game over message: Displays “Game Over” when the snake dies.

🛠️ How It Works

The game is structured into multiple classes for clear organization:

1. Snake (snake.py)

   - Handles the snake’s segments, movement, growth, and direction changes.

   - The head’s heading determines the direction of .forward() movement.

   - New segments are added at the tail’s position, which then follow the rest of the body naturally.

2. Food (food.py)

   - A small yellow circle that appears in a random location on the screen.

   - Calls refresh() to randomly reposition after being eaten.

3. Scoreboard (scoreboard.py)

   - Displays the current score at the top of the screen.

   - Updates dynamically when the snake eats food.

   - Shows “Game Over” when the snake collides with walls or itself.

4. main.py

   - Sets up the game screen with turtle.Screen().

   - Handles the main game loop: moving the snake, detecting collisions, updating the scoreboard, and refreshing the screen.

   - Uses screen.tracer(0) and screen.update() for smooth animation.

   - Uses time.sleep(0.1) to control the snake’s speed.

🎮 Controls

| Key         | Action     |
| ----------- | ---------- |
| Up Arrow    | Move Up    |
| Down Arrow  | Move Down  |
| Left Arrow  | Move Left  |
| Right Arrow | Move Right |

📦 Requirements

- Python 3.x
- No additional packages are required (uses built-in turtle and random modules).

🚀 How to Run

1. Clone or download the repository.

2. Make sure all files (main.py, snake.py, food.py, scoreboard.py) are in the same directory.

3. Run the game:
```
python main.py
```
4. The game window will open. Use the arrow keys to control the snake.

5. The game ends if the snake hits a wall or itself.

🔧 Notes

- The snake grows when it eats the food, which is placed randomly within the window boundaries.

- The scoreboard updates in real-time to reflect the current score.

- The snake cannot reverse direction directly (prevents instant collisions).