🎨 Hirst Painting

A colorful 10×10 dot grid inspired by Damien Hirst’s spot paintings, created using Python’s turtle graphics. Each dot is randomly colored from a curated RGB palette, making a fun and dynamic pattern.

🖼 Preview

- 10 rows × 10 columns of dots

- Each dot has a random color

- Clean grid layout with spacing of 50 pixels

🛠 Requirements

- Python 3.x

- Built-in turtle module (no extra installation needed)

▶️ How to Run

1. Clone the repository:

        git clone https://github.com/Banteas/hirst-painting.git
        cd hirst-painting



2. Run the program:

        python main.py


3. A turtle window will open and draw the grid.

4. Close the window by clicking on it when finished.

📂 Project Structure 

    hirst-painting/
    │
    ├── main.py        # Main program file
    ├── image.jpg      # Example output of the dot grid
    └── README.md      # Project documentation


🎨 How it works

- A turtle object (franklin) moves across the canvas.

- Nested loops calculate positions for each dot.

- random.choice(color_list) picks a random RGB color for each dot.

- colormode(255) allows RGB tuples to be used.
- The result is a colorful, randomized grid reminiscent of Hirst’s spot paintings.

🤝 Ideas for Extension

- Increase grid size or spacing.

- Experiment with larger dot diameters.

- Add animation or random walks between the dots.

- Try different color palettes for different moods.

- Generate patterns like spirals, diagonals, or gradients.