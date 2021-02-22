def storeStudentAnswersInFile(fileName, correctAnswersList):
    studentAnswersFile = open(fileName, "w")
    numberOfQuestions = len(correctAnswersList)

    for currentUserAnswerIndex in range( numberOfQuestions ):
       userAnswer =  input( "Please enter your answer" + 
                           str((currentUserAnswerIndex + 1)) + ": ")

       studentAnswersFile.write(userAnswer + "\n")

       #studentAnswersFile.close()

def readStudentAnswersFromFileToList(fileName):
           studentAnswersList =[]  #this is an empty list

           studentAnswersFile = open( fileName, "r")

           for studentAnswer in studentAnswersFile:
               studentAnswer.rstrip("\n")
               studentAnswersList.append(studentAnswer)

           return studentAnswersList



def determineNumberOfCorrectAnswers(examCorrectAnswersList, studentAnswersList):
    correctAnswers = 0
    numberOfQuestions = len( examCorrectAnswersList )
    for currentExamQuestionIndex in range ( numberOfQuestions):
        if studentAnswersList[ currentExamQuestionIndex ] == examCorrectAnswersList[ currentExamQuestionIndex]:
            correctAnswers = correctAnswers + 1
            return correctAnswers



def determineNumberOfIncorrectAnswers ( numberOfCorrectAnswers, numberOfQuestions):
    numberOfIncorrectAnswers = numberOfQuestions - numberOfCorrectAnswers
    return numberOfIncorrectAnswers


def getIncorrectlyAnsweredQuestionNumbers( numberOfQuestions ):
    if studentAnswersList[ currentExamQuestionIndex ] != examCorrectAnswersList[ currentExamQuestionIndex ]:
        incorrectQuestionNumbersList.append(currentExamQuestionIndex + 1)
        return incorrectQuestionNumbersList


def studentPassedExam( passMark, numberOfCorrectAnswers):
        if len(numberOfCorrectAnswers) >= passMark:
            return True
        else:
            return False



def printValuesInList(anyList):
    for currentValueIndex in range( len(anyList)):
        print( anyList[currentValueIndex], end = ", ")



def printResults(numberofCorrectyAnsweredQuestions, numberOfIncorrectlyAnsweredQuestions, incorrectlyAnsweredQuestionNumbersList):


    print("\nNumber of correctly Answered questions: " + str(numberOfCorrectlyAnsweredQuestions), "Number of incorrectly answered questions:" + str(numberOfIncorrectlyAnsweredQuestions), sep = "\n")

    print()

    printValuesInList(incorrectlyAnsweredQuestionsNumbersList)

   

def main():
    correctAnswersList = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

    NUMBER_OF_QUESTIONS = len(correctAnswersList)

    FILE_NAME = "studentAnswers.txt"

    PASS_MARK = 15

    storeStudentAnswersInFile( FILE_NAME, correctAnswersList )

    studentAnswersList = readStudentAnswersFromFileToList(FILE_NAME)

    print

    numberOfCorrectAnswers =  determineNumberOfCorrectAnswers(correctAnswersList, studentAnswersList)

    numberOfIncorrectAnswers = determineNumberOfIncorrectAnswers(numberOfCorrectAnswers, NUMBER_OF_QUESTIONS)

    incorrectQuestionNumbersList = getIncorrectlyAnsweredQuestionNumbers(correctAnswersList, studentAnswersList)

    printResults( numberOfCorrectAnswers, numberOfIncorrectAnswers, incorrectQuestionNumbersList )

    if studentPassedExam(PASS_MARK, numberOfCorrectAnswers ):
        print("The student passed the exam")
    else:
            print("The student failed the exam")




main()



#This is a drivers License Program that calculates a students grade
# python standard to not exceed 79 characters in a line
#Author: Heather Whittlesey



           





