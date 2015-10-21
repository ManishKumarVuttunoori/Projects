import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves
import random
my_color=""   ### Max player's color
time_set = False
safe= False
king=False
init_time = 0    ## for storing the initial time
init_moves=0   ### for storing the initial no. of moves
### CUSTOM EVALUATION FUNCTION FOR MINIMAX WITH PRUNING
###  custom evaluation function considers the no. of pawns, no. of kings, no. of kings and pawns present in edges(considered safe) of the board and assignes weights to the differences of corresponding values
###  co - effeicients for the differences were given based on experimentation 
### Im storing the counts of pawns and kings of both players in the dictionaries
### based on the time left and moves remaining w.r.t to the initial time and moves, I am changing the behaviour of the evaluation function using safe, king variables
def simple_eval(board):
    global my_color
    color= my_color
    opponentColor = gamePlay.getOpponentColor(color)
    value = 0
    # Loop through all board positions
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
                
        if board[x][y].upper() == color.upper():
            value = value + 1
        elif board[x][y].upper() == opponentColor.upper():
            value = value - 1

    return value

def curr_evaluation(board):
    global my_color, safe, king
    color = my_color
    opponentColor = gamePlay.getOpponentColor(color)
    global lower, check
    noOfPawns={'r':0, 'w':0}
    noOfKings={'R':0, 'W':0}
    noOfSafePawns= {'r':0, 'w':0}
    noOfSafeKings={'R':0, 'W':0}
               
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x,y = xy[0], xy[1]            
        if board[x][y] == color:
            noOfPawns[color]+=1
        elif board[x][y] == opponentColor:
            noOfPawns[opponentColor]+=1
        elif board[x][y]==color.upper():
            noOfKings[color.upper()]+=1
        elif board[x][y]==opponentColor.upper():
            noOfKings[opponentColor.upper()]+=1
        if piece in [1,4,9,17,25,8, 16, 24, 5,13,21,12,20,28,29,30,32]:    ## checking the nodes in edges
            if board[x][y] == color:
                noOfSafePawns[color]+=1
                noOfPawns[color]-=1
            elif board[x][y] == opponentColor:
                noOfSafePawns[opponentColor]+=1
                noOfPawns[opponentColor]-=1
            elif board[x][y]==color.upper():
                noOfSafeKings[color.upper()]+=1
                noOfKings[color.upper()]-=1
            elif board[x][y]==opponentColor.upper():
                noOfSafeKings[opponentColor.upper()]+=1
                noOfKings[opponentColor.upper()]-=1
    value= 0
    if safe==True and king==False:
        value+=(noOfPawns[color] -noOfPawns[opponentColor])*1.5 +   1.5*(noOfSafePawns[color] - noOfSafePawns[opponentColor]) 
    elif king==True and safe==False:
        value+= 2*(noOfKings[color.upper()]- noOfKings[opponentColor.upper()]) +  1.4*(noOfSafePawns[color] - noOfSafePawns[opponentColor]) #(noOfPawns[color] -noOfPawns[opponentColor])*1.5 +
    elif safe==True and king==True:
        value+=(noOfPawns[color] -noOfPawns[opponentColor])*1.5 + 1.5*(noOfKings[color.upper() ] ) +  1*(noOfSafePawns[color] - noOfSafePawns[opponentColor]) +1*(noOfSafeKings[color.upper()] - noOfSafeKings[opponentColor.upper()]) #'''- noOfKings[opponentColor.upper()]'''
    else:
        value+= (noOfPawns[color] -noOfPawns[opponentColor])*1.5 + 2*(noOfKings[color.upper()] - noOfKings[opponentColor.upper()]) + 1.5*(noOfSafePawns[color] - noOfSafePawns[opponentColor]) +1.5*noOfSafeKings[color.upper()]
    return value

## using depth 5
def nextMove(board, color, time, movesRemaining):
    global my_color, init_time, time_set, init_moves, safe, king
    my_color = color
    print "My move turn\n"
    moves = getAllPossibleMoves(board, color)
    #Trying to find the move where I have best score
    bestMove=None

    if len(moves)==1:              ## return the move when only a single move is present 
        bestMove = moves[0]
        print "return the only move left\n"
    else:                                 ## more than one possible move is present.
        best = None
        depth =4
        heuristic = curr_evaluation
        alpha = -float('inf')
        beta = float('inf')
        if not time_set:            ## recording the time given so as to split into intervals
            time_set = True
            init_time = time
            init_moves=movesRemaining
        
        if init_time*3/4 <=time and time<init_time:   ##game is in the first quarter
            if movesRemaining>146:
                depth = random.randrange(1,3)
                safe=False
                king=True
            elif movesRemaining>130 and movesRemaining <=146:
                depth =random.randrange(4,7)
                safe=True
                king=True
            elif movesRemaining > init_moves*2/3 and movesRemaining<=130:
                depth=random.randrange(5,7)
                king= True
                safe=True
            else:
                depth=5
                king=True
                safe=False
        elif init_time/2 <=time and time< init_time*3/4:     ## game is in the second quarter
            if movesRemaining>init_moves/3 and movesRemaining< 2*init_moves/3:
                depth = 5
                safe=True
                king = True
            elif movesRemaining>0 and movesRemaining <=init_moves/3:
                depth = 6
                 
        elif time>init_time/4 and time<= init_time/2:
            safe=False
            king= True
            if movesRemaining>init_moves/3 and movesRemaining< 2*init_moves/3:
                depth = 6
            elif movesRemaining>0 and movesRemaining <=init_moves/3:
                depth = 5
                king=True
                safe=True
            else:
                depth=5
        else:
            depth=5
            king=True
            safe=True
            ##heuristic =
            
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)        
            moveVal = miniMax(newBoard,depth,float('inf'), alpha, True, gamePlay.getOpponentColor(color), heuristic)  ### we have already evaluated Max's childs here so, its Min's turn to make a move on each of these childs, so min turn is true.
            if best == None or moveVal > best:
                bestMove = move
                best = moveVal
                alpha = moveVal
           
    return bestMove
   
###minimax function with alpha beta pruning implemented    initial values are -infinity and infinity for alpha and beta respectively
## 
def miniMax(board, depth, beta, alpha, minPlayerTurn, color, heuristic): ## returns best value for max or min
    moves = getAllPossibleMoves(board, color)

    if depth==0 or len(moves)==0:  ## base condition   return if depth is reached or if there are no moves present
        return heuristic(board)

    if minPlayerTurn==False:   # Max player
        
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)           
            alpha= max(alpha, miniMax(newBoard, depth-1, beta, alpha, True, gamePlay.getOpponentColor(color), heuristic))       ###recursive call to Min player
            if alpha >=beta:     ## prune 
                break
        return alpha
    elif minPlayerTurn==True:
        ## Min Player's turn        
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard, move)
            beta= min(beta, miniMax(newBoard, depth-1, beta, alpha, False, gamePlay.getOpponentColor(color), heuristic))  ###recursive call to Max player
            if alpha >=beta:    # prune
                break
        return beta
       
