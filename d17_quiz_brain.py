class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # return a boolean to show whether more questions are yet to be asked
        return self.question_number < len(self.question_list)

    def next_question(self):
        # getting hold of each question whose index is determined by 'question_number'
        current_question = self.question_list[self.question_number]

        # we can get hold of the question by:
        # question_list.text

        # instead of writing self.question_number++, we'll simply increment the q_no by 1 already and it will not affect
        # the code
        self.question_number += 1

        # show the question to the user and ask for the answer(true/false)
        user_answer = input(f'Q{self.question_number}. {current_question['text']} \ntrue/false :')

        # check whether the question is correctly answered or not
        self.check_answer(user_answer, current_question['answer'])

    def check_answer(self, user_answer, correct_answer):
        # check if the input is same as the correct answer or not
        if user_answer.lower() == correct_answer.lower():
            print(f"That's correct!")
            self.score += 1
        else:
            print(f"That's wrong!")
            print(f"The correct answer is {correct_answer}")

        # display the score
        # also leave a line's worth of space before proceeding to the next question
        print(f"The current score is {self.score}/{self.question_number}\n")






