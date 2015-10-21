## gets the empty position after checking if any corner positions are empty and if any pawn of human is present in the same row.
##If nothing is found, it returns a empty location coordinates based on whether the center is occupied by human or bot

## Manish Kumar Vuttunoori   ( manivutt)

import random

def get_empty_pos(map, choice):
    odd= False
    center = False
    if map[1][1]==player:
        center = True
    odd_places = [map[0][1],map[1][0],map[1][2], map[2][1]]
    if " " in odd_places and center==False:
        rand_int = random.randrange(len(odd_places))
        while odd_places[rand_int]!= " ":
            rand_int = random.randrange(len(odd_places))
        if rand_int==0:
            return 0,1
        elif rand_int==1:
            return 1,0
        elif rand_int==2:
            return 1,2
        elif rand_int==3:
            return 2,1
        odd = True
    if odd== False:
        center = False
        diag_2 = [map[2][0], map[0][2]]
        empty_list = []
        count = diag_2.count(" ")
        for i in range(3):
            if i!=1 and map[i][abs(2-i)]==choice and  map[i][i]==" ":           
                return i,i
        #print "1st part unsuccessful"    
        if count!=0:               
            ind = diag_2.index(" ")
            if ind==0 and map[2][2]==choice:
                return 2,0
            else:
                return 0,2
        else:
            for i in range(3):
                for j in range(3):
                    if map[i][j]==" ":
                        empty_list.append((i,j))
            if(len(empty_list)!=0):
                rand_int = random.randrange(len(empty_list))
                return empty_list[rand_int]
    return False                

 ## checks if the board is empty and returns true or false                                  
def isBoardEmpty(map):
    for i in range(3):
        if map[i].count(" ")==3:
            pass
        else:
            return False
    return True

empty_board = False

##checks all the rows to see if the player(can be a human or computer) can make a winning move if not returns false    
def check_row(map, choice):
    for i in range(3):
        if map[i].count(choice)==2 and " " in map[i]:
            return i,map[i].index(" ")
    return False

##checks all the columns to see if the player(can be a human or computer) can make a winning move if not returns false        
def check_col(map, choice):
    
    for i in range(3):
        count = 0
        empty= False
        for j in range(3):
            if map[j][i]==choice:
                count+=1
            if map[j][i]==" ":
                empty =  j,i
        if count==2 and empty!=True:
            return empty
    return False

##checks all the diagonals to see if the player(can be a human or computer) can make a winning move if not returns false    
def check_diag(map, choice):
    count=0
    empty = False
    for i in range(3):
        if map[i][i]==choice:
            count+=1
        if map[i][i]==" ":
            empty = i,i
    if count==2 and empty!=False:
            return empty    
    
    diag_2 = [map[2][0],map[1][1], map[0][2]]   
    if diag_2.count(choice)==2 and " " in diag_2:
        ind = diag_2.index(" ")
        if ind==0:
            return 2,0
        elif ind==1:
            return 1,1
        elif ind==2:
            return 0,2
    else:
        return False

## prints the board
def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""

## prints exiting messages based on who the winner is or if the game is draw
def is_winner(turn, draw=False):
    if draw==False:
        if turn==comp:
            print  "I win!!! Better luck next time :) Here is the final move I made..."
        else:
            print  "Congrats! you win!  :) and here is the deciding move..."
    else:
        print "Well...its a draw..Here is the final deciding move of the game"
    print_board()   
    return

##checks if the game is over 
def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            is_winner(turn)
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        is_winner(turn)
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        is_winner(turn,True)       
        return True        
    return False

#Determining the player's turn starts from here
turn = "X"
comp=""

while True:
    player = raw_input("Which player do you want to be?? ").upper().strip()
    if player not in ['X','O']:
        print "You have entered an invalid input please enter again. Please either  X or O"
    elif player=='X':
       comp='O'
       break
    else:
       comp='X'
       break
      
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False


while done != True:
    print_board()
    
    print turn, "'s turn"
    print

    moved = False
    while moved != True:
        if turn==player:
            print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
            print "7|8|9"
            print "4|5|6"
            print "1|2|3"
            print
        if(turn!=comp):                           # If its player's tun then display the options on the screen
            try:
                pos = input("Select: ")
                if pos <=9 and pos >=1:
                    Y = pos/3
                    X = pos%3
                    if X != 0:
                        X -=1
                    else:
                        X = 2
                        Y -=1
                      
                    if map[Y][X] == " ":
                        map[Y][X] = turn
                        moved = True
                        done = check_done()

                        if done == False:
                            if turn == player:
                                turn = comp
                                  
            except:
                print "You need to enter a numeric value"

        else:
            #print "here comes the rules part!!!"
            print
            if(isBoardEmpty(map)):
                map[1][1] = comp
                moved= True
            else:
                if map[1][1]==" ":
                    if empty_board== False:
                        map[1][1] = comp
                        moved = True
                        empty_board = True
                    else:    
                        my_list = [(0,0),(2,2),(2,0),(0,2)]
                        space = [map[0][0],map[2][2],map[2][0],map[0][2]]
                        if " " in space:
                            rand = random.randrange(len(my_list))
                            coord = my_list[rand]                        
                            while map[coord[0]][coord[1]]!= " " :
                                rand = random.randrange(len(my_list))
                                coord = my_list[rand]
                            map[coord[0]][coord[1]] = comp
                            moved =True
                else: #map[1][1]==player:
                    coord = check_diag(map,comp)
                    if coord!= False:
                        map[coord[0]][coord[1]] = comp
                        moved = True
                    else:
                        coord = check_row(map,comp)
                        if coord!= False:
                            map[coord[0]][coord[1]] = comp
                            moved = True
                        else:
                            coord = check_col(map,comp)
                            if coord!= False:
                                map[coord[0]][coord[1]] = comp
                                moved = True
                            else:
                                coord = check_row(map,player)
                                if coord!= False:
                                    map[coord[0]][coord[1]]=comp
                                    moved = True
                                else:
                                    coord = check_col(map,player)
                                    if coord!= False:
                                        map[coord[0]][coord[1]]=comp
                                        moved = True
                                    else:
                                        coord = check_diag(map,player)
                                        if coord!= False:
                                            map[coord[0]][coord[1]]=comp
                                            moved = True
                                        else:
                                            #print "I am in here..."
                                            coord = get_empty_pos(map, player)
                                            if coord!= False:
                                                map[coord[0]][coord[1]] = comp
                                                moved = True
                                                
            done = check_done()
            if done==False:
               if turn==comp:
                  turn=player

              
