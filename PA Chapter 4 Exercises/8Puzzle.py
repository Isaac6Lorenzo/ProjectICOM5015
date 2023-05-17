import numpy
import time
import random
import math

failed = False

# manhattan_distance
def getManhattanDistance(board):
    distance = 0
    for i in range(len(board)):
        distance += abs(i/3 - board[i]/3) + abs(i%3 - board[i]%3)
    return distance
#======================================================================
# Steepest Hill Climbing
def step_steepestHillClimbing(board):
    for i in range(len(board)):
        if board[i] == 0:
            break
    distanceBoard = {}
    if i >= 3:
        upBoard = list(board)
        upBoard[i] = board[i-3]
        upBoard[i-3] = 0
        distanceBoard[i-3] = getManhattanDistance(upBoard)
    if i < 6:
        downBoard = list(board)
        downBoard[i] = board[i+3]
        downBoard[i+3] = 0
        distanceBoard[i+3] = getManhattanDistance(downBoard)
    if i%3 != 0:
        leftBoard = list(board)
        leftBoard[i] = board[i-1]
        leftBoard[i-1] = 0
        distanceBoard[i-1] = getManhattanDistance(leftBoard)
    if (i+1)%3 != 0:
        rightBoard = list(board)
        rightBoard[i] = board[i+1]
        rightBoard[i+1] = 0
        distanceBoard[i+1] = getManhattanDistance(rightBoard)
    
    shortestDistance = getManhattanDistance(board)
    for point,value in distanceBoard.items():
        # "<=" means "not worse than" situation
        # plain
        if value <= shortestDistance:
            shortestDistance = value
    
    shortestDistancePoints = []
    for point,value in distanceBoard.items():
        if value == shortestDistance:
            shortestDistancePoints.append(point)
    
    # can not find a steeper move
    # we have come to the peek(local optimization)
    if len(shortestDistancePoints) == 0:
        # print "local optimization"
        global failed
        failed = True
        return board
    
    random.shuffle(shortestDistancePoints)
    board[i] = board[shortestDistancePoints[0]]
    board[shortestDistancePoints[0]]= 0
    return board

def solution_steepestHillClimbing(board):
    # For each case, there are only several situations using this solution.
    # In average, we will reach a local optimization within 100 steps
    # or fall into a infinite loop (a plain) within 100 steps.
    maxRound = 100
    count = 0
    while True:
        count += 1
        collisionNum = getManhattanDistance(board)
        global failed
        # print count, collisionNum
        if collisionNum == 0:
            return board
        board = step_steepestHillClimbing(board)
        if failed:
            return board
        if(count >= maxRound):
            # for i in range(0,len(board)):
            #     print board[i]
            failed = True
            return board

def Steepest_HillClimbing():
    title = "EightPuzzle_StepHC"
    startTime = time.time()
    successCase = 0
    failedCase = 0
    totalCase = 0
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"

    with open("eightPuzzleCases.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            global failed
            failed = False
            totalCase += 1
            board = []
            for col in row.split():
                board.append(int(col))
            board = solution_steepestHillClimbing(board)
            if failed:
                text += "failed!"
                failedCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if failed == False:
                text += "     " + str(getManhattanDistance(board))
            else:
                text += "                " + str(getManhattanDistance(board))

            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failedCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)*100) + '%\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)

    return text

#======================================================================

# First Choice Hill Climbing
def step_FirstChoiceHillClimbing(board):
    global failed
    for i in range(len(board)):
        if board[i] == 0:
            break
    distance = getManhattanDistance(board)
    maxRound = 50 # the expected rounds to produce all the 4 directions
    count = 0
    while True:
        count += 1
        if(count >= maxRound):
            failed = True
            return board
        randCase = random.randint(0,4)
        if randCase == 0:
            if i >= 3:
                upBoard = list(board)
                upBoard[i] = board[i-3]
                upBoard[i-3] = 0
                if getManhattanDistance(upBoard) < distance:
                    return upBoard
        elif randCase == 1:
            if i < 6:
                downBoard = list(board)
                downBoard[i] = board[i+3]
                downBoard[i+3] = 0
                if getManhattanDistance(downBoard) < distance:
                    return downBoard
        elif randCase == 2:
            if i%3 != 0:
                leftBoard = list(board)
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                if getManhattanDistance(leftBoard) < distance:
                    return leftBoard
        else:    
            if (i+1)%3 != 0:
                rightBoard = list(board)
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                if getManhattanDistance(rightBoard) < distance:
                    return rightBoard
        
    return board

def solution_FirstChoiceHillClimbing(board):
    global failed
    maxRound = 200
    count = 0
    while True:
        collisionNum = getManhattanDistance(board)
        if collisionNum == 0:
            return board
        board = step_FirstChoiceHillClimbing(board)
        count += 1
        if(count >= maxRound):
            failed = True
            return board

def FirstChoice_HillClimbing():
    title = "EightPuzzle_FCHC"
    startTime = time.time()
    successCase = 0
    failedCase = 0
    totalCase = 0
    global failed
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"
        
    with open("eightPuzzleCases.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            failed = False
            totalCase += 1
            board = []
            for col in row.split():
                board.append(int(col))
            board = solution_FirstChoiceHillClimbing(board)
            if failed:
                text += "failed!"
                failedCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if failed == False:
                text += "     " + str(getManhattanDistance(board))
            else:
                text += "                " + str(getManhattanDistance(board))

            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failedCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)
    return text

#======================================================================

# Random Restart Hill Climbing
def step_RandomHillClimbing(board):
    for i in range(len(board)):
        if board[i] == 0:
            break
    while True:
        randCase = random.randint(0,4)
        if randCase == 0:
            if i >= 3:
                upBoard = list(board)
                upBoard[i] = board[i-3]
                upBoard[i-3] = 0
                return upBoard
        elif randCase == 1:
            if i < 6:
                downBoard = list(board)
                downBoard[i] = board[i+3]
                downBoard[i+3] = 0
                return downBoard
        elif randCase == 2:
            if i%3 != 0:
                leftBoard = list(board)
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                return leftBoard
        else:    
            if (i+1)%3 != 0:
                rightBoard = list(board)
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                return rightBoard
        
    return board

def solution_RandomHillClimbing(board):
    global failed
    maxRound = 500000
    count = 0
    while True:
        distance = getManhattanDistance(board)
        if distance == 0:
            return board
        board = step_RandomHillClimbing(board)
        count += 1
        if(count >= maxRound):
            failed = True
            return board


def Random_HillClimbing():
    title = "EightPuzzle_RHC"
    startTime = time.time()
    successCase = 0
    failedCase = 0
    totalCase = 0
    global failed
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"
    
    with open("eightPuzzleCases.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            failed = False
            totalCase += 1
            board = []
            for col in row.split():
                board.append(int(col))
            board = solution_RandomHillClimbing(board)
            if failed:
                text += "failed!"
                failedCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if failed == False:
                text += "     " + str(getManhattanDistance(board))
            else:
                text += "                " + str(getManhattanDistance(board))

            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failedCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)
    return text

#======================================================================

# Simmulated Annealing
def step_SimulatedAnnealing(board):
    temperature = len(board)
    annealingRate = 0.95
    
    for i in range(len(board)):
        if board[i] == 0:
            break
    distance = getManhattanDistance(board)
    temperature = max(temperature * annealingRate, 0.02)
    while True:
        randCase = random.randint(0,4)
        if randCase == 0:
            if i >= 3:
                upBoard = list(board)
                upBoard[i] = board[i-3]
                upBoard[i-3] = 0
                if getManhattanDistance(upBoard) < distance:
                    return upBoard
                else:
                    deltaE = getManhattanDistance(upBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return upBoard
        elif randCase == 1:
            if i < 6:
                downBoard = list(board)
                downBoard[i] = board[i+3]
                downBoard[i+3] = 0
                if getManhattanDistance(downBoard) < distance:
                    return downBoard
                else:
                    deltaE = getManhattanDistance(downBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return downBoard
        elif randCase == 2:
            if i%3 != 0:
                leftBoard = list(board)
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                if getManhattanDistance(leftBoard) < distance:
                    return leftBoard
                else:
                    deltaE = getManhattanDistance(leftBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return leftBoard
        else:    
            if (i+1)%3 != 0:
                rightBoard = list(board)
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                if getManhattanDistance(rightBoard) < distance:
                    return rightBoard
                else:
                    deltaE = getManhattanDistance(rightBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return rightBoard
                    
    return board


def solution_SimulatedAnnealing(board):
# the success rate will increase by increasing the maxRound
    global failed
    maxRound = 500000
    count = 0
    while True:
        collisionNum = getManhattanDistance(board)
        if collisionNum == 0:
#            print(count)
            return board
        board = step_SimulatedAnnealing(board)
        count += 1
        if(count >= maxRound):
            failed = True
            return board

def SimulatedAnnealing():
    title = "EightPuzzle_SA"
    startTime = time.time()
    successCase = 0
    failedCase = 0
    totalCase = 0
    global failed
    text = "\n\n"
    text += title + " Solution:\n\n"
    text += "Board" + "           " + "Function H\n\n"
   
    with open("eightPuzzleCases.txt", "r") as file:
        for row in file:
            print("case: ", totalCase)
            failed = False
            totalCase += 1
            board = []
            # print("start")
            for col in row.split():
                board.append(int(col))
            board = solution_SimulatedAnnealing(board)
            # print("end")

            if failed:
                text += "failed!"
                failedCase += 1
            else:
                successCase += 1
                for col in range(len(board)):
                    text += str(board[col]) + " "
            if failed == False:
                text += "     " + str(getManhattanDistance(board))
            else:
                text += "                " + str(getManhattanDistance(board))
            
            text += "\n"
        print("End Proccesing Board" + "\n")
    
    endTime = time.time()
    clock = endTime - startTime
    text += "\nTotal time in second: " + str(clock) + '\n'
    text += "Total time in minute: " + str(clock/60) + '\n'
    text += "\nTotal Case: " + str(totalCase) + '\n'
    text += "Success Case: " + str(successCase) + '\n'
    text += "Fail Case: " + str(failedCase) + '\n'
    text += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    text += "" + '\n'
    text += "" + '\n'
    print(text)
    return text

#======================================================================
#======================================================================
#======================================================================

def Search_Steepest_HillClimbing():
    print("Steepest_HillClimbing")
    textSteepHC = Steepest_HillClimbing()
    writerFile("StepHC", textSteepHC)
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

#======================================================================
#======================================================================
#======================================================================

def writerFile(strName, text):
    tittle = "Solution_8Puzzle"
    file = open(tittle + strName + ".txt", 'w')
    file.write(text)
    file.close()
    return 0

#======================================================================
#======================================================================
#======================================================================

def generator(amount):
    case = ""
    with open('eightPuzzleCases.txt', 'w') as the_file:

        for x in numpy.nditer(range(amount)):
            line = numpy.random.default_rng().choice(9, size=9, replace=False)
            for i in numpy.nditer(line):
                case += str(i)+ ' '
            case += '\n'
        the_file.write(case)
        the_file.close()

def main():
    start = time.time()
    # size of list of exercises
    n = 10
    
    # create n-exercise of 8-Puzzle problem
    generator(n)
    print("End create an list of exercises")

    # ok
    # super fast method
    Search_Steepest_HillClimbing()

    # ok
    # super fast method
    Search_FirstChoice_HillClimbing()

    # ok
    # medium low method
    Search_Random_HillClimbing()
    
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

        
if __name__ == '__main__':
    main()
