
class Question:
  def __init__(self,text,answer):
    self.text = text
    self.answer = answer
newQuestion = Question("text", "answer")
print(newQuestion.answer)
print(newQuestion.text)