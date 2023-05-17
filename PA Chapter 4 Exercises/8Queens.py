import random
import time
import math

fail = False
# ===========================================================
def main():
    start = time.time()
    # size of list of exercises
    n = 100
    
    # create n-exercise of 8-Queens problem
    create_QueenBoard(n)
    print("End create an list of exercises")

    # ok
    # super fast method
    Search_Steepest_HillClimbing()

    # ok
    # medium low method
    Search_Random_HillClimbing()

    # ok
    # super fast method
    Search_FirstChoice_HillClimbing()
    
    # not ok with print
    # super low method
    Search_SimulatedAnnealing()

    end = time.time()
    clock = end - start
    title ="List of exercises: " + str(n) + ", " + "time execution: " + str(clock)
    writerFile("Time_Execution", title)

    print("Execution of the Program\n")
    print("Time of Execution: ", clock)
    return 0

# ===========================================================
# ===========================================================
# ===========================================================
def Search_Steepest_HillClimbing():
    print("Steepest_HillClimbing")
    textStepHC = Steepest_HillClimbing()
    writerFile("StepHC", textStepHC)
    return 0

def Search_Random_HillClimbing():
    print("Random_HillClimbing")
    textRHC = Random_HillClimbing()
    writerFile("RHC", textRHC)
    return 0
    
def Search_FirstChoice_HillClimbing():
    print("FirstChoice_HillClimbing")
    textFCHC = FirstChoice_HillClimbing()
    writerFile("FCHC", textFCHC)
    return 0
    
def Search_SimulatedAnnealing():
    print("Simulated_Annealing")
    textSA = SimulatedAnnealing()
    writerFile("SA", textSA)
    return 0

# ===========================================================
# ===========================================================
# ===========================================================
def writerFile(strName, text):
    tittle = "Solution_8Queen"
    file = open(tittle + strName + ".txt", 'w')
    file.write(text)
    file.close()
    return 0

def create_QueenBoard(count):
    file = open("boardQueen.txt", "w")
    board = ""
    while count > 0:
        count -= 1
        for col in range(7):
            board += str(random.randint(0,7)) + " "
            if col == 6 and count == 0:
                board += str(random.randint(0,7))
            elif col == 6:
                board += str(random.randint(0,7)) + "\n"
    file.write(board)
    file.close()

def getAttackCount(board):
    attack = 0
    for col in range(len(board)):
        for anotherCol in range(col+1, len(board)):
            if board[col] == board[anotherCol]:
                attack += 1 # attack horizontal
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                attack += 1 # attack diagonal
            # elif attack ==0:
                # attack vertical
    return attack

# ===========================================================
# ===========================================================
# ===========================================================
def Random_HillClimbing():
    title = "EightQueens_RHC"
    startTime = time.time()
    successCase = 0
    failCase = 0
    totalCase = 0
    global fail
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"
    
    with open("boardQueen.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            fail = False
            totalCase += 1
            board = []
            for col in row.split():
                board.append(int(col))
            board = solution_RHC(board)
            if fail:
                text += "fail!"
                failCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if fail == False:
                text += "     " + str(getAttackCount(board))
            else:
                text += "                " + str(getAttackCount(board))

            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)
    return text

def solution_RHC(board):
    maxRound = 500000
    count = 0
    global fail

    while True:
        collisionNum = getAttackCount(board)
        if collisionNum == 0:
            return board
        
        while True:
            row = random.randint(0,len(board)-1)
            col = random.randint(0,len(board)-1)
            if board[col] != row:
                board[col] = row
                break

        count += 1
        if(count >= maxRound):
            fail = True
            return board

# ===========================================================
def FirstChoice_HillClimbing():
    title = "EightQueens_FCHC"
    startTime = time.time()
    successCase = 0
    failCase = 0
    totalCase = 0
    global fail
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"
        
    with open("boardQueen.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            fail = False
            totalCase += 1
            board = []
            for col in row.split():
                board.append(int(col))
            board = solution_FCHC(board)
            if fail:
                text += "fail!"
                failCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if fail == False:
                text += "     " + str(getAttackCount(board))
            else:
                text += "                " + str(getAttackCount(board))

            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)
    return text

def solution_FCHC(board):
    maxRound = 200 # the expected number to find a solution
    count = 0
    global fail

    while True:
        attack = getAttackCount(board)
        if attack == 0:
            return board
   
        newRound = 1000 
        newCount = 0
        while True:
            newCount += 1
            if(newCount >= newRound):
                fail = True
                break
            row = random.randint(0,len(board)-1)
            col = random.randint(0,len(board)-1)
            if board[col] == row:
                continue
            newRow = board[col]
            board[col] = row
            if getAttackCount(board) <= attack: 
                break
            board[col] = newRow       
            
        if fail:
            return board
        count += 1
        if(count >= maxRound):
            fail = True
            return board
        
# ===========================================================
def SimulatedAnnealing():
    title = "EightQueens_SA"
    startTime = time.time()
    successCase = 0
    failCase = 0
    totalCase = 0
    global fail
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"
   
    with open("boardQueen.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            fail = False
            totalCase += 1
            board = []
            # print("start")
            for col in row.split():
                board.append(int(col))
            board = solution_SA(board)
            # print("end")

            if fail:
                text += "fail!"
                failCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if fail == False:
                text += "     " + str(getAttackCount(board))
            else:
                text += "                " + str(getAttackCount(board))
            
            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)
    return text

def solution_SA(board):
    # the success rate will increase by increasing the maxRound
    maxRound = 1000000
    count = 0
    global fail

    while True:
        attack = getAttackCount(board)
        if attack == 0:
            return board

        temperature = len(board)**2
        annealingRate = 0.95
        while True:
            row = random.randint(0,len(board)-1)
            col = random.randint(0,len(board)-1)
            attack = getAttackCount(board)
            originRow = board[col]
            board[col] = row
            newAttack = getAttackCount(board)
            temperature = max(temperature * annealingRate, 0.02)
            if newAttack < attack:
                # return board
                break
            else:
                deltaE = newAttack - attack
                acceptProbability = min(math.exp(deltaE / temperature), 1)
                if random.random() <= acceptProbability:
                    break
                else:
                    board[col] = originRow

        count += 1
        if(count >= maxRound):
            fail = True
            return board
    
# ===========================================================
def Steepest_HillClimbing():
    title = "EightQueens_StepHC"
    startTime = time.time()
    successCase = 0
    failCase = 0
    totalCase = 0
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"

    with open("boardQueen.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            global fail
            fail = False
            totalCase += 1
            board = []
            for col in row.split():
                board.append(int(col))
            board = solution_StepHC(board)
            if fail:
                text += "fail!"
                failCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if fail == False:
                text += "     " + str(getAttackCount(board))
            else:
                text += "                " + str(getAttackCount(board))

            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)

    return text

def solution_StepHC(board):
    maxRound = 200
    count = 0
    global fail
    while True:
        attack = getAttackCount(board)
        if attack == 0:
            return board
        
        collisionNumBoard = []
        smallestCollisionNum = getAttackCount(board)
        for col in range(len(board)):
            for row in range(len(board)):
                if board[col] == row:
                    continue
                originRow = board[col]
                board[col] = row
                point = row, col
                attack = getAttackCount(board)
                item = point, attack
                collisionNumBoard.append(item)
                board[col] = originRow
        
        for point,value in collisionNumBoard:
            if value < smallestCollisionNum:
                smallestCollisionNum = value
        
        smallestCollisionPoints = []
        for point,value in collisionNumBoard:
            if value == smallestCollisionNum:
                smallestCollisionPoints.append(point)
        
        if len(smallestCollisionPoints) == 0:
            fail = True
            return board
        
        random.shuffle(smallestCollisionPoints)
        board[smallestCollisionPoints[0][1]]=smallestCollisionPoints[0][0]
        
        count += 1
        if(count >= maxRound):
            fail = True
            return board

# ===========================================================
# ===========================================================
# ===========================================================
if __name__ == "__main__":
    main()
