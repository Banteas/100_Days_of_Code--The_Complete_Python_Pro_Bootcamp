import turtle
import pandas as pd
from state import State
from scoreboard import Scoreboard

# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

state_writer = State()
scoreboard = Scoreboard()

# Game loop
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 Correct",
        prompt="What's another State?"
    )

    if answer_state is None or answer_state.title() == "Exit":  # user clicked Cancel
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)

        states_date = pd.DataFrame({"Missed States": states_to_learn})
        states_date.to_csv("states_to_learn.csv", index=False)
        break

    answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        state_writer.state_create(answer_state, x, y)

        guessed_states.append(answer_state)
        scoreboard.increase_score()

