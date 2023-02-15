import os
rows, cols = (5, 5)

def populate(classRecord):

    print("Input 5 Quiz Scores For 5 Students")
    print("===================================")

    for row in range(0, rows):
        for col in range(0, cols):
            
            score = 0

            while True:

                while True:
                    try:
                        score = int(input("Input Student {0} Score for Quiz {1}: ".format(row+1,col+1)))
                    
                    except:
                        print("Score must be a number!")
                        continue
                    break

                if score < 0:
                    print("Score is invalid!")
                    continue
                break
            
            classRecord[row][col] = score

def printClassRecord(classRecord):

    i = 1

    for row in classRecord:
        
        print("Student {0}: ".format(i) + str(row)) 
        i+= 1

def getStudentAvg(classRecord):

    avg = []
   
    for row in range(0, rows):

        sum = 0

        for col in range(0, cols):

            sum += classRecord[row][col]
        sum = sum / cols
        avg.append(sum) 

    print("Student Average:")
    print("======================")

    for i in range(rows):
        print("Student {0}: ".format(i+1) + str(avg[i]))    

def getQuizAvg(classRecord):

    avg = []
   
    for col in range(0, cols):

        sum = 0

        for row in range(0, rows):

            sum += classRecord[row][col]
        sum = sum / rows
        avg.append(sum) 

    print("Quiz Average:")
    print("======================")

    for i in range(cols):
        print("Quiz {0}: ".format(i+1) + str(avg[i]))                 

def findStudentLowest(classRecord):

    score =[]

    while True:
 
        studNum = int(input("Input Student Number (1-5): "))
                    
        if studNum not in (1,2,3,4,5):
            print("Student number is invalid!")
            continue
        break

    for col in range(0, cols):
        score.append(classRecord[studNum-1][col])

    print("Student " + str(studNum) + " Lowest Score: " + str(min(score)))        

def findQuizLowest(classRecord):

    score =[]

    while True:
 
        quizNum = int(input("Input Quiz Number (1-5): "))
                    
        if quizNum not in (1,2,3,4,5):
            print("Quiz number is invalid!")
            continue
        break

    for row in range(0, rows):
        score.append(classRecord[row][quizNum-1])

    print("Quiz " + str(quizNum) + " Lowest Score: " + str(min(score)))        

def findStudentHighest(classRecord):

    score =[]

    while True:
 
        studNum = int(input("Input Student Number (1-5): "))
                    
        if studNum not in (1,2,3,4,5):
            print("Student number is invalid!")
            continue
        break

    for col in range(0, cols):
        score.append(classRecord[studNum-1][col])

    print("Student " + str(studNum) + " Highest Score: " + str(max(score)))        

def findQuizHighest(classRecord):

    score =[]

    while True:
 
        quizNum = int(input("Input Quiz Number (1-5): "))
                    
        if quizNum not in (1,2,3,4,5):
            print("Quiz number is invalid!")
            continue
        break

    for row in range(0, rows):
        score.append(classRecord[row][quizNum-1])

    print("Quiz " + str(quizNum) + " Highest Score: " + str(max(score)))        

def main():
    os.system('cls')
 
    classRecord = [[0 for i in range(cols)] for j in range(rows)]

    populate(classRecord)

    
      
    while True:
            os.system('cls')
 
            printClassRecord(classRecord)

            print("Menu:")
            print("=========================")
            print("1.) Calculate average score of each student")
            print("2.) Calculate average score of each quiz")
            print("3.) Find Lowest Student Score")
            print("4.) Find Lowest Quiz Score")
            print("5.) Find Lowest Student Score")
            print("6.) Find Lowest Quiz Score")
            print("\n")

            #take input1
            choice = input("Enter Choice: ")

            #check choice
            if choice in ('1', '2', '3', '4','5','6'):

                if choice == '1':
                    getStudentAvg(classRecord)
                
                elif choice == '2':
                    getQuizAvg(classRecord)
                
                elif choice == '3':
                    findStudentLowest(classRecord)
                
                elif choice == '4':
                    findQuizLowest(classRecord)
                
                elif choice == '5':
                    findStudentHighest(classRecord)
                
                elif choice == '6':
                    findQuizHighest(classRecord)

                while True:
                    check = input("Do you want to do another operation? ([1]Yes/[0]No):")
                    
                    if check not in ('0','1'):
                        continue
                    else:
                        break
                
                if check == '0':
                    break
            else:
                print("Invalid Option!")
        
if __name__ == '__main__':
    main();