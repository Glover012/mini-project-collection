import requests, html, random

class Question:
    def __init__(self, tp, difficulty, category, question, correct_answer, incorrect_answers, points):
        self.tp = tp
        self.difficulty = difficulty
        self.category = category
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.points = points
        self.answerList = self.incorrect_answers
        self.answerList.append(self.correct_answer)
        random.shuffle(self.answerList)

class Quiz:
    questionsList = []

    def __init__(self, qAmount="1", qCategory="", qDifficulty="", qType="" ):
        # https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean
        self.qAmount = str(qAmount)
        self.qCategory = str(qCategory)
        self.qDifficulty = str(qDifficulty).lower()
        self.qType = str(qType).lower()
        self.url = f"https://opentdb.com/api.php?amount={self.qAmount}{f"&category={self.qCategory}" if self.qCategory != "" else ""}{f"&difficulty={self.qDifficulty}" if self.qDifficulty != "" else ""}{f"&type={self.qType}" if self.qType != "" else ""}"
        print(self.url)
        # Methods
        self.questionsData = self.getQuestionsDataFromApi(self.url)
        self.questionsDataToObjects(self.questionsData)

    def getQuestionsDataFromApi(self, url):
        questionsData = None
        response = requests.get(url)
        if response.ok == True:
            questionsData = response.json()
        return questionsData

    def questionsDataToObjects(self, questionsData):
        points = None
        for questionParams in questionsData["results"]:
            if questionParams["difficulty"] == "hard": points = 3
            elif  questionParams["difficulty"] == "medium": points = 2
            elif  questionParams["difficulty"] == "easy": points = 1

            self.questionsList.append(
            Question(
            questionParams["type"],
            questionParams["difficulty"],
            questionParams["category"],
            # html.unescape to remove html entities
            html.unescape(questionParams["question"]),
            html.unescape(questionParams["correct_answer"]),
            html.unescape(questionParams["incorrect_answers"]),
            points
            ))

    def dispalyQuestion(self, question, iq=1): # iq - Iterate questions
        ia = 1 # Iterate answers
        print(f"{iq}. {question.question}")
        print(f" Difficulty - {question.difficulty.capitalize()} Points: {question.points}")
        print(f" Correct answer: {question.correct_answer}")

        # For multiple choice
        if question.tp == "multiple":
            for answer in question.answerList:
                print(f"\t{ia}. {answer}")
                ia += 1
            else:
                ia = 1
    
    def printAllQuestions(self):
        iq = 1
        for question in self.questionsList:
            self.dispalyQuestion(question, iq)
            iq+=1

    def runQuiz(self):
        iq = 1 # Question iterator
        points = 0
        maxPoints = 0
        correctAnswers = 0
        for question in self.questionsList:
            maxPoints += question.points
            self.dispalyQuestion(question, iq)
            iq+=1

            if question.tp == "boolean":
                answer = str(input("Input answer: T/F: ")).lower()
                if answer == "t": answer = "True"
                elif answer == "f": answer = "False"

                if answer == question.correct_answer:
                    points += question.points
                    correctAnswers += 1

            elif question.tp == "multiple":
                answer = int(input("Input answer: [1-4]: "))
                if question.answerList[answer-1] == question.correct_answer:
                    points += question.points
                    correctAnswers += 1

        scorePrecentageValue = int(points/(maxPoints)*100)
        print(f"Quiz finished! Score: {scorePrecentageValue}%")
        print(f"Score: {points}/{maxPoints}")
        print(f"Good answers: {correctAnswers}/{iq-1}")

quiz = Quiz(qAmount="3")
quiz.runQuiz()
