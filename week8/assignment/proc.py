from random import *
import math

minRang = 1
maxRang = 100

operatorByIdArr = {
    0: '+',
    1: '-',
    2: '*'
}

operatorFuncByIdArr = {
    0: lambda num1, num2: num1 + num2,
    1: lambda num1, num2: num1 - num2,
    2: lambda num1, num2: num1 * num2
}

worngProblemsArr = []
problemsArr = []


class Problem:
    def __init__(self, num1, num2, operatorId):
        self.num1 = num1
        self.num2 = num2
        self.operatorId = operatorId
        self.userAnswer = '-1'

    def getProblem(self):
        return str(self.num1) + " " + operatorByIdArr[self.operatorId] + " " + str(self.num2) + " = ?"

    def getAnswer(self):
        func = operatorFuncByIdArr[self.operatorId]
        return func(self.num1, self.num2)

    def setUserAnswer(self, userAnswer):
        self.userAnswer = userAnswer

    def isCorrect(self):
        return self.userAnswer == str(self.getAnswer())


print("********************** Welcome **********************")
isPlay = 1

while isPlay:
    problem = Problem(randint(minRang, maxRang),
                      randint(minRang, maxRang), randint(0, 2))
    print(problem.getProblem())
    userInput = input()
    problem.setUserAnswer(userInput)
    if problem.isCorrect():
        print("Good job! Your answer is correct")
    else:
        worngProblemsArr.append(problem)
        print("You worng! :/ The correct answer is: " + str(problem.getAnswer()))
    problemsArr.append(problem)
    isValidInput = 0

    while not isValidInput:
        print("Do you wanna try again? [Y/N]:")
        userInput = input()

        if userInput[0].lower() == 'n':
            isPlay = 0
            isValidInput = 1
        elif userInput[0].lower() == 'y':
            isValidInput = 1
        else:
            print("Worng input, please try again...")
            isValidInput = 0

print("********************** Summary **********************")
for answer in worngProblemsArr:
    print(answer.getProblem().replace("?", str(answer.userAnswer)) +
          " (" + str(answer.getAnswer()) + ")")

numOfProblems = len(problemsArr)
numOfCorrectAnsweres = numOfProblems - len(worngProblemsArr)
avgOfCorrection = math.floor((numOfCorrectAnsweres * 100) / numOfProblems)


print("You have answered correctly " + str(numOfCorrectAnsweres) +
      " out of " + str(numOfProblems) + " (" + str(avgOfCorrection) + "%)")
