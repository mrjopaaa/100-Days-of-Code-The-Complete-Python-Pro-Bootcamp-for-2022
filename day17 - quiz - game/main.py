from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question = key
    text = question.get("text")
    answer = question.get("answer")
    question_model = Question(text, answer)
    question_bank.append(question_model)


quiz = QuizBrain(question_bank)

quiz.next_question()

while quiz.still_has_questions():
    """The questions will be provided in console while there are questions in 
       question list"""
    quiz.next_question()

print("You've completed the quiz.")
print(f"You've got {quiz.score}/{quiz.question_number} correct answers.")