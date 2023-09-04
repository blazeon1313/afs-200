import random



class TriviaQuestions():

    def __init__(self, question, category, difficulty_level, correct_answer, incorrect_answer, id_iter):
        self.question = question
        self.category = category
        self.difficulty_level = difficulty_level
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answer
        self.id_iter = id_iter

    def getQuestion(self):
        return self.question
    
    def getCategory(self):
        return self.category
    
    def getDifficulty(self):
        return self.difficulty_level
    
    def getCorrect(self):
        return self.correct_answer
    
    def getIncorrect(self):
        return self.incorrect_answer
    
    def getId(self):
        return self.id_iter

    def getShuffledAnswers(self):

        questionList = self.incorrect_answer
        questionList.append(self.correct_answer)

        random.shuffle(questionList)

        return questionList
    
    def __str__(self):
        rtnstr = self.question
        rtnstr += " "
        rtnstr += self.correct_answer
        rtnstr += " "
        rtnstr += str(self.incorrect_answer)

        return rtnstr