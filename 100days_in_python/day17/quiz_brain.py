class QuizBrain:
    def __init__(self, q_list):
        self.questions_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.questions_number < len(self.question_list)

    def next_question(self):
        current_question= self.question_list[self.questions_number]
        self.questions_number += 1
        user_answer=input(f"Q.{self.questions_number}:{current_question.text}. (True/False) :")
        self.check_answers(user_answer, current_question.answer)

    def check_answers(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("that' wrong!")
        print(f"your current score is: {self.score}/{self.questions_number}")
        print(f"The correct answer is {correct_answer}")
        print("\n")