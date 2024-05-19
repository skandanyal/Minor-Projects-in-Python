from d17_data import question_data
from d17_question_model import Question
from d17_quiz_brain import QuizBrain

# create a question bank to store the data set
question_bank = []

for question in question_data:
    # here, question is the individual dictionary already and it need not be accessed through an index
    new_question = Question(question['text'], question['answer'])

    # append this new question into the question bank
    question_bank.append(new_question)

# load the data set into the class QuizBrain
quiz = QuizBrain(question_data)

# display the current question
# quiz.next_question()

# display the subsequent questions
while quiz.still_has_questions():
    quiz.next_question()

# once the quiz has ended, display the final score
print("The quiz is over")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

