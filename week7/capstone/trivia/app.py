from flask import Flask, request, render_template
import requests
import json
from socket import timeout
from urllib import response
from triviagame import TriviaGame 
from triviaquestion import TriviaQuestions

def getData(triviaQuestions):
    URL = "https://opentdb.com/api.php?amount=10&category=18&type=multiple"

    try:
        response = requests.get(URL, timeout=25)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    print(triviaQuestions, "line 25 print")


myTriviaGame = TriviaGame()

jsonData = getData("triviaQuestions")

idCounter = 0

for data in jsonData["results"]:
    question = data["question"]
    correct_answer = data["correct_answer"]
    incorrect_answer = data["incorrect_answers"] 
    category = data["category"]
    difficulty_level = data["difficulty"]
    id_iter = idCounter

    newQuestion = TriviaQuestions(question, category, difficulty_level, correct_answer, incorrect_answer, id_iter)
    
    myTriviaGame.addQuestions(newQuestion) 
    idCounter += 1

myTriviaGame.getAllQuestions()

app = Flask(__name__)

@app.route("/")
def home():
    myTrivia = myTriviaGame.getAllQuestions()
    
    return render_template("questions.html", results = myTrivia)
    
@app.route("/score", methods = ["POST"])
def getScore():
    myTrivia = myTriviaGame.getAllQuestions()
    correctQuestion = []
    incorrectQuestion = []
    for question in myTrivia:

        inputValue = request.form.get(str(question.id_iter))

        if(inputValue == question.correct_answer):
            correctQuestion.append(question)
        else:
            incorrectQuestion.append(question)

    results = {"correct": correctQuestion, "incorrect": incorrectQuestion}
    return render_template('answers.html', results = results)

if __name__ == "__main__":
    app.run()