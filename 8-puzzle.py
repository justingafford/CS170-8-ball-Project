import sys, copy

# this is the goal state i.e. when the iteration stops
goal = [['1','2','3'],['4','5','6'],['7','8',' ']]

def main() :
    input = puzzleUser() # user input
    theAlgorithm = algorithmChoice() # algorithm choice
    solvePuzzle(input,theAlgorithm) # solve the puzzle

# user input
def puzzleUser():
    # as per the specifications we have to set a default puzzleUser
    default = [['1','2','3'],['4','8',' '],['7','6', '5']]
    # puzzleChoice is the puzzle that our algorithm operates on
    puzzleChoice = []
    print ("Welcome to Justin Gafford's (SID 862052189) 8 puzzle solver")
    
    while 1:
        userChoice = input("Type '1' for default puzzle, '2' for your own, or '3' to quit.\n")
        # if user chooses 1 we load puzzleChoice with the default puzzle.
        if(userChoice == '1'):
            print ("OK, using default puzzle.\n")
            puzzleChoice = default
            return puzzleChoice
        
        # user populates puzzle themselves
        elif (userChoice == '2'):
            print ("Enter your puzzle, use a zero to represent the blank:\n")
            
            # row 1 input
            row1 = input("Enter the first row, use spaces between numbers: ")
            # makes sure that row1 is split by spaces
            row1 = row1.split(' ')
            # we convert the 0 to a blank space
            if (row1.count('0') == 1):
                row1[row1.index('0')] = ' '
            
            # row 2 input
            row2 = input("Enter the second row, use spaces between numbers: ")
            # makes sure that row1 is split by spaces
            row2 = row2.split(' ')
            # we convert the 0 to a blank space
            if (row2.count('0') == 1):
                row2[row2.index('0')] = ' '
        
            # row 3 input
            row3 = input("Enter the third row, use spaces between each number: ")
            # makes sure that row1 is split by spaces
            row3 = row3.split(' ')
            # we convert the 0 to a blank space
            if (row3.count('0') == 1):
                row3[row3.index('0')] = ' '
            
            # assemble user input
            puzzleChoice.append(row1)
            puzzleChoice.append(row2)
            puzzleChoice.append(row3)
            #print (puzzleChoice)
            return puzzleChoice
        #if the userChoice is 3, we exit the program       
        elif (userChoice == '3'):
            sys.exit(0)      
          
def algorithmChoice():
    print ("1. Uniform Cost Search")
    print ("2. A* with the Misplaced Tile heuristic")
    print ("3. A* with the Eucledian distance heuristic")
    
    while 1:
        algoChoice = input("Enter your choice of algorithm:\n")
        if(algoChoice == '1'):
            return "ucSearch"
        elif(algoChoice == '2'):
            return "mtHeuristic"
        elif(algoChoice == '3'):
            return "edHeuristic"
    return algoChoice
    
def goalCheck(puzzleChoice):
    return goal == puzzleChoice  
    
# this is the data structure of our program, as we enqueue puzzle states with nodes
class node:
    # initailize to 0
    def __init__(aNode):
        aNode.heuristic = 0
        aNode.depth = 0 
    # overide print function to print out puzzles
    def puzzlePrint(aNode):
        print (aNode.puzzleSquare[0][0], aNode.puzzleSquare[0][1], aNode.puzzleSquare[0][2])
        print (aNode.puzzleSquare[1][0], aNode.puzzleSquare[1][1], aNode.puzzleSquare[1][2])
        print (aNode.puzzleSquare[2][0], aNode.puzzleSquare[2][1], aNode.puzzleSquare[2][2])
    def puzzleSquareDefine(aNode,puzzleChoice):
        aNode.puzzleSquare = puzzleChoice

def mtHeuristic(puzzleChoice):
    misplaceNum = 0
    # 3x3 matrix so x and y have a range of 3
    for x in range(3):
        for y in range(3):
            # dont check the empty space
            if(puzzleChoice[x][y] != ' '):
                if(puzzleChoice[x][y] != goal[x][y]):
                    misplaceNum = misplaceNum + 1 
    return misplaceNum
    
def edHeuristic(puzzleChoice):
    eucDist = 0
    puzzleNums = ['1', '2', '3', '4', '5', '6', '7', '8']
    # search through the all 8 numbers in the puzzle
    for x in puzzleNums:
        for i in range(3):
            for j in range(3):
                # we search where we are in relation to goal
                if (x == goal[i][j]):
                    gRow = i
                    gCol = j
                # we search where we are in relation to the puzzleChoice
                if (x == puzzleChoice[i][j]):
                    pRow = i
                    pCol = j
        # caluclating the eucledian distance using puzzle and goal rows and columns
        eucDist = eucDist + (pow((gRow - pRow),2) + pow((gCol - pCol),0))
    return eucDist
    
def puzzleMove(puzzleChoice):
    possibleMoves = []
    # We have to account for 4 movements including: up,down,left,right
    
    moveUp = copy.deepcopy(puzzleChoice)
    # move blank tile up
    for x in puzzleChoice:
        # this code checks where our blank tile is
        if (x.count(' ') == 1):
            # we have to make sure its not on top so moving the tile up is legal
            if (x != moveUp[0]):
                blankIndex = x.index(' ')
                # the blank is on second row
                if(x == puzzleChoice[1]):
                    moveUp[1][blankIndex] = moveUp[0][blankIndex]
                    moveUp[0][blankIndex] = ' '
                    possibleMoves.append(moveUp)
                # the blank is on third row
                else:
                    moveUp[2][blankIndex] = moveUp[1][blankIndex]
                    moveUp[1][blankIndex] = ' '
                    possibleMoves.append(moveUp)

    moveDown = copy.deepcopy(puzzleChoice)
    # move blank down
    for x in puzzleChoice:
        # this code checks where our blank tile is
        if (x.count(' ') == 1):
            # we have to make sure its not on bottom so moving the tile down is legal
            if (x != puzzleChoice[2]):
                blankIndex = x.index(' ')
                # the blank is on second row
                if(x == puzzleChoice[0]):
                    moveDown[0][blankIndex] = moveDown[1][blankIndex]
                    moveDown[1][blankIndex] = ' '
                    possibleMoves.append(moveDown)
                # the blank is on third row
                else:
                    moveDown[1][blankIndex] = moveDown[2][blankIndex]
                    moveDown[2][blankIndex] = ' '
                    possibleMoves.append(moveDown)
            
    moveLeft = copy.deepcopy(puzzleChoice)
    # move blank left
    for x in moveLeft:
        # this code checks where our blank tile is
        if (x.count(' ') == 1):
            # we have to make sure its not on left so moving the tile left is legal
            if (x.index(' ') != 0):
                blankIndex = x.index(' ')
                x[blankIndex] = x[blankIndex - 1]
                x[blankIndex - 1] = ' '
                possibleMoves.append(moveLeft)

    moveRight = copy.deepcopy(puzzleChoice)
    # move blank right
    for x in moveRight:
        # this code checks where our blank tile is
        if (x.count(' ') == 1):
            # we have to make sure its not on right so moving the tile right is legal           
            if (x.index(' ') != 2):
                blankIndex = x.index(' ')
                x[blankIndex] = x[blankIndex + 1]
                x[blankIndex + 1] = ' '
                possibleMoves.append(moveRight)
                
    return possibleMoves


#adapted from: https://www.geeksforgeeks.org/python-program-for-selection-sort/
def selectionSort(queuePuzzle):
    # Traverse through all array elements
    for i in range(len(queuePuzzle)) :
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(queuePuzzle)): 
            if (queuePuzzle[min_idx].heuristic + queuePuzzle[min_idx].depth > \
                queuePuzzle[j].heuristic + queuePuzzle[j].depth): 
                    min_idx = j 
        # Swap the found minimum element with  
        # the first element         
        queuePuzzle[i], queuePuzzle[min_idx] = queuePuzzle[min_idx], queuePuzzle[i] 
        return queuePuzzle

    
def solvePuzzle(puzzleChoice,algorithmChoice):
    # number of expanded nodes
    numExpanded = 0
    # max size of queue
    queueSize = 0
    # puzzle that is in the queue
    queuePuzzle = []
    # initialize the puzzle(create new node)
    firstNode = node()
    firstNode.puzzleSquareDefine(puzzleChoice)
    # set the depth of our origin node
    firstNode.depth = 0
    
    # next we define our heuristics
    if(algorithmChoice == "ucSearch"):
        firstNode.heuristic = 1
    elif(algorithmChoice == "mtHeuristic"):
        firstNode.heuristic = mtHeuristic(firstNode.puzzleSquare)
    elif(algorithmChoice == "edHeuristic"):
        firstNode.heuristic = edHeuristic(firstNode.puzzleSquare)
    queuePuzzle.append(firstNode)
    
    # now that we have our initial puzzle, we move the puzzle until its solved
    while 1:
        if(len(queuePuzzle) == 0):
            print ("Puzzle search failed")
            sys.exit(0)
            
        #We then queue up the next node in the queue
        nextNode = node()
        nextNode.puzzleSquare = queuePuzzle[0].puzzleSquare
        nextNode.heuristic = queuePuzzle[0].heuristic
        nextNode.depth = queuePuzzle[0].depth
        #print the depth and heuristic as in the project specifications
        print ("The best node to expand with g(n) = ", nextNode.depth ,
            " and h(n) = ", nextNode.heuristic, " is...")
        nextNode.puzzlePrint()
        print ("Expanding this node...")
        
        #we then pop the front of the queue
        queuePuzzle.pop(0)
        
        #As per A* properties, we check goalstate after we pop a node
        if(goalCheck(nextNode.puzzleSquare)):
            #If goal is reached we print out stats of simulation
            print ("Goal!!!")
            nextNode.puzzlePrint()
            print ("To solve this problem the search algorithm expande a total of "
                , numExpanded, " nodes")
            print ("The maximum number of nodes in the queue at any one time:"
                , queueSize)
            return
        
        #We move the puzzle left,right,up or down
        swapNodes = puzzleMove(nextNode.puzzleSquare)
        
        #Each possible move is added to the queue(tree of all possible moves)
        for x in swapNodes:
            branchNode = node()
            branchNode.puzzleSquareDefine(x)
            #as before we define our heuristics(it'll be the same)
            if(algorithmChoice == "ucSearch"):
                branchNode.heuristic = 1
            elif(algorithmChoice == "mtHeuristic"):
                branchNode.heuristic = mtHeuristic(branchNode.puzzleSquare)
            elif(algorithmChoice == "edHeuristic"):
                branchNode.heuristic = edHeuristic(branchNode.puzzleSquare)
                
            #because we are adding more nodes, we increase the depth
            branchNode.depth = nextNode.depth + 1
            #after we adjust the depth, we add the node to the queue
            queuePuzzle.append(branchNode) 
            
            #since we expanded another node, increment numExpanded
            numExpanded = numExpanded + 1
            
            #update if we have a greater length of nodes than are in queueSize
            if (len(queuePuzzle) > queueSize):
                queueSize = len(queuePuzzle)
        queuePuzzle = selectionSort(queuePuzzle)
        
if __name__ == "__main__":
    main()
