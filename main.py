from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    q_position = question_data.index(question)
    q_sentence = question_data[q_position]["text"]
    q_response = question_data[q_position]["answer"]
    new_q = Question(q_sentence, q_response)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()



