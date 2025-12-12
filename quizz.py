"""
Project Requirements:
The user will be promted with some questions, and they need to decide if it is True or False
There will be a scoring as well.

Initialize the Question objects from the data table. Questions should be objects, in Question_model.

"""

from resource.question_model import Question
from resource.data import quesiton_data

quesiton_bank = []
for question in quesiton_data:
    question_text = quesiton["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    quesiton_bank.append(new_question)

