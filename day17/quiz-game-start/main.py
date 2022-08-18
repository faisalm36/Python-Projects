from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

#5:33 
for question in question_data:
  question_text = question["text"]
  question_ans = question["answer"]
  new_question = Question(question_text,  question_ans)
  question_bank.append(new_question)
while quiz.still_has_questions():  
  quiz.next_question()


 