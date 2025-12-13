"""
Project Requirements:
The user will be promted with some questions, and they need to decide if it is True or False
There will be a scoring as well.

Initialize the Question objects from the data table. Questions should be objects, in Question_model.

"""

from resources.question_model import Question
from resources.data import question_data, question_data2
from resources.quiz_brain import QuizBrain

quesiton_bank = []
#for question in question_data: Commented out as this is the first interation
for question in question_data2: # Second iteration
    #question_text = question["text"] Commented out as this is the first interation
    question_text = question["question"] # Second iteration
    #question_answer = question["answer"] Commented out as this is the first interation
    question_answer = question["correct_answer"] # Second iteration
    new_question = Question(question_text, question_answer)
    quesiton_bank.append(new_question)

quiz = QuizBrain(quesiton_bank)
while quiz.still_has_questions():
    quiz.next_question()   

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(quesiton_bank)}") 