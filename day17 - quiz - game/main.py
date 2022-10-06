from question_model import Question
from data import question_data

# Write a for loop to iterate over the question data
# Create a question object from each entry in question_data
# Append each question object to the question bank

question_bank = []

for key in question_data:
    question = key
    text = question.get("text")
    answer = question.get("answer")
    q_m = text, answer
    question_model = Question(text, answer)
    question_bank.append(question_model)
