from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(self.window, text=f"Score: 0 ", fg="white",bg=THEME_COLOR,pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(150,125,
                                                     text = "",
                                                     fill= THEME_COLOR,
                                                     width = 280,
                                                     font= ("Arial",20,"italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.false_button = Button(self.window, image= false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row = 2, column = 1,pady=20)
        self.true_button = Button(self.window, image= true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(row = 2, column = 0, pady= 20)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz")
            self.canvas.config(bg="white")
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.update_score()
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, self.get_next_question)
    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
