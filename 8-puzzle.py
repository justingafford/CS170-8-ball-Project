import sys, copy

# this is the goal state i.e. when the iteration stops
goal = [['1','2','3'],['4','5','6'],['7','8',' ']]

def main() :
    input = puzzleUser() #user input
    theAlgorithm = algorithmChoice() #algorithm choice
    solvePuzzle(input,theAlgorithm) #solve the puzzle

#user input
def puzzleUser():
    #as per the specifications we have to set a default puzzleUser
    default = [['1',' ','3'],['5','2','4'],['7','8', '6']]
    puzzleChoice = []
    print ("Welcome to Justin Gafford's (SID 862052189) 8 puzzle solver")
    
    while 1:
        userChoice = input("Type '1' for default puzzle, '2' for your own, or '3' to quit.\n")
        #if user chooses 1 we load puzzleChoice with the default puzzle.
        if(userChoice == '1'):
            print ("OK, using default puzzle.\n")
            puzzleChoice = default
            return puzzleChoice
        
        #user populates puzzle themselves
        elif (userChoice == '2'):
            print ("Enter your puzzle, use a zero to represent the blank:\n")
            
            #row 1 input
            row1 = input("Enter the first row, use spaces between numbers: ")
            #makes sure that row1 is split by spaces
            row1 = row1.split(' ')
            #we convert the 0 to a blank space
            if (row1.count('0') == 1):
                row1[row1.index('0')] = ' '
            
            #row 2 input
            row2 = input("Enter the second row, use spaces between numbers: ")
            #makes sure that row1 is split by spaces
            row2 = row2.split(' ')
            #we convert the 0 to a blank space
            if (row2.count('0') == 1):
                row2[row2.index('0')] = ' '
        
            #row 3 input
            row3 = input("Enter the third row, use spaces between each number: ")
            #makes sure that row1 is split by spaces
            row3 = row3.split(' ')
            #we convert the 0 to a blank space
            if (row3.count('0') == 1):
                row3[row3.index('0')] = ' '
            
            #assemble user input
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
    print ("3. A* with the Euclediandistance heuristic")
    
    while 1:
        algoChoice = input("Enter your choice of algorithm:\n")
        if(algoChoice == '1'):
            return "ucSearch"
        elif(algoChoice == '2'):
            return "mtHeuristic"
        elif(algoChoice == '3'):
            return "edHeuristic"
    return algoChoice

if __name__ == "__main__":
    main()
