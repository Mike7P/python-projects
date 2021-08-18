from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question = q['text']
    answer = q['answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print(f"Well done! You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

