import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(timer)
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer",fg=GREEN)
    tick_label.config(text="")






# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        title_label.config(text="Long Break", fg=RED)

        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    time_str = f"{count_min:02d}:{count_sec:02d}"

    canvas.itemconfig(timer_text, text=time_str)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(window, width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)


timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(window, text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(window, fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)


window.mainloop()
