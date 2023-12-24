class QuizBrain:
    
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True / False)?: ")
        self.check_answer(response, current_question.answer)

    def still_has_questions(self):
        return self.question_number in range(len(self.questions_list))
    
    def check_answer(self,user_answer,question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("Nice Job! You got it right")
        else:
            print("That's wrong.")
        print(f"Your score is: {self.score} / {self.question_number}")
        print("\n")