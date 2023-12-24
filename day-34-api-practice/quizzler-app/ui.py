from tkinter import *
from quiz_brain import QuizBrain

BG_COLOR = "#454D66"
TEXT_BOX_COLOR = "#E6E3D3"
FONT = ("Arial", 20, "italic")
SUCCESS_COLOR = "#83BD75"
ERROR_COLOR = "#AC7D88"



class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Trivia Game")
        self.window.config(padx=20,pady=20, bg=BG_COLOR)

        #Quiz Text
        self.canvas = Canvas(width=300,height=250, bg=TEXT_BOX_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text="Quiz Game", 
            font=FONT, 
            fill=BG_COLOR
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        #Buttons
        image_true = PhotoImage(file="images/true.png")
        image_false = PhotoImage(file="images/false.png")

        self.button_true = Button(
            image = image_true, 
            highlightthickness=0, 
            highlightbackground=BG_COLOR, 
            bg=BG_COLOR,
            command=self.true_pressed
            )
        self.button_false = Button(
            image = image_false, 
            highlightthickness=0, 
            highlightbackground=BG_COLOR,
            bg=BG_COLOR,
            command=self.false_pressed
            )

        self.button_true.grid(row=2, column=0, padx=20)
        self.button_false.grid(row=2,column=1, padx=20)
        
        #labels
        self.label_score = Label(text=f"Score: 0", background=BG_COLOR, fg=TEXT_BOX_COLOR)
        self.label_score.grid(row=0,column=1)
        
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.label_score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg=TEXT_BOX_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()       
        else:
            q_text = f"You've completed the quiz!\n Your final score was {self.quiz.score}/{self.quiz.question_number}"
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))
        

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=SUCCESS_COLOR)
        else:
            self.canvas.config(bg=ERROR_COLOR)
        self.window.after(1000,self.get_next_question)
        
        
