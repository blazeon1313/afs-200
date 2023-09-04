class TriviaGame():
    def __init__(self):
        self.questions = []
    
    def addQuestions(self, question):
        self.questions.append(question)

    def getAllQuestions(self):

        return self.questions