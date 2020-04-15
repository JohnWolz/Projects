#---------------------------------------------------------
# John Wolz
# 102-51-920
# October 28th, 2019
# Assignment #2: Intelligent Othello Player
# This program implements the game of Othello and implements
# an intelligent Othello player using classical AI with MinMax
# searching and Alphabeta pruning
#---------------------------------------------------------

white = "O"
black = "■"
valid = "▒"

search_depth = 5

global board

board = [[" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," ",white,black," "," "," "],
         [" "," "," ",black,white," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "]]

def PrintBoard():
    print(" ║A║B║C║D║E║F║G║H║")
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("1║"+board[0][0] + "║"+board[0][1] + "║"+board[0][2] + "║"+board[0][3] + "║"+board[0][4] + "║"+board[0][5] + "║"+board[0][6] + "║"+board[0][7] + "║" + "  White: " + str(CountPoints(white)) + "  Black: " + str(CountPoints(black)))
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("2║"+board[1][0] + "║"+board[1][1] + "║"+board[1][2] + "║"+board[1][3] + "║"+board[1][4] + "║"+board[1][5] + "║"+board[1][6] + "║"+board[1][7] + "║")
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("3║"+board[2][0] + "║"+board[2][1] + "║"+board[2][2] + "║"+board[2][3] + "║"+board[2][4] + "║"+board[2][5] + "║"+board[2][6] + "║"+board[2][7] + "║")
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("4║"+board[3][0] + "║"+board[3][1] + "║"+board[3][2] + "║"+board[3][3] + "║"+board[3][4] + "║"+board[3][5] + "║"+board[3][6] + "║"+board[3][7] + "║" + "      White = " + white)
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("5║"+board[4][0] + "║"+board[4][1] + "║"+board[4][2] + "║"+board[4][3] + "║"+board[4][4] + "║"+board[4][5] + "║"+board[4][6] + "║"+board[4][7] + "║" + "      Black = " + black)
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("6║"+board[5][0] + "║"+board[5][1] + "║"+board[5][2] + "║"+board[5][3] + "║"+board[5][4] + "║"+board[5][5] + "║"+board[5][6] + "║"+board[5][7] + "║" + "   ValidSpace = " + valid)
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("7║"+board[6][0] + "║"+board[6][1] + "║"+board[6][2] + "║"+board[6][3] + "║"+board[6][4] + "║"+board[6][5] + "║"+board[6][6] + "║"+board[6][7] + "║" + "Enter moves in format \"A1\"")
    print("═╬═╬═╬═╬═╬═╬═╬═╬═╣")
    print("8║"+board[7][0] + "║"+board[7][1] + "║"+board[7][2] + "║"+board[7][3] + "║"+board[7][4] + "║"+board[7][5] + "║"+board[7][6] + "║"+board[7][7] + "║")
    print("═╩═╩═╩═╩═╩═╩═╩═╩═╝")

def Search(x, y, hor, ver, color):
    if x+hor < 8 and x+hor >-1 and y+ver < 8 and y+ver >-1:
    
        if board[x+hor][y+ver] == " ": # locates a blank space
            try:
                spot = board[x-hor][y-ver]
            except:
                return
            c = 2 # counter
            while spot == color: # makes a path in the opposite direction of blank space to determine if the blank space is a valid move
                try:
                    spot = board[x-(c * hor)][y-(c*ver)]
                except:
                    return
                c += 1
            if (color == white and spot == black) or (color == black and spot == white):
               board[x+hor][y+ver] = valid

def Pathfind(x, y, hor, ver, color, opp_color): # Similar to search, except changes all pieces in the path

    if x+hor > 7 or x+ver < 0 or y+ver > 7 or y+ver < 0: # the edge of the board is reached
        return False
    elif board[x+hor][y+ver] == color: # the path is completed because a piece of the players color was found
        return True
    elif board[x+hor][y+ver] == opp_color:
        change = Pathfind(x+hor,y+ver,hor,ver,color,opp_color)
        if change == True:
            board[x+hor][y+ver] = color
            return True
    else:
        return False
        
def DeterminePlayableSpaces(color):
    # removes confusion about color needing to be opp_color
    if color == black: 
        color = white
    else:
        color = black
    
    # loops through board to find pieces of the correct color
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == color: # the current space on the board is a space of the opposite color
                k = 1
                while k <= 8: # checks for open spaces in all 8 squares next to current space
                    if k == 1: # path going up
                        Search(i, j, 0, -1, color)
                    elif k == 2: # path going up and right
                        Search(i, j, 1, -1, color)
                    elif k == 3: # path going right
                        Search(i, j, 1, 0, color)
                    elif k == 4: # path going down and right
                        Search(i, j, 1, 1, color)
                    elif k == 5: # path going down
                        Search(i, j, 0, 1, color)
                    elif k == 6: # path going down and left
                        Search(i, j, -1, 1, color)
                    elif k == 7: # path going left
                        Search(i, j, -1, 0, color)
                    elif k == 8: # path going up and left
                        Search(i, j, -1, -1, color)

                    k+=1

def MakeMove(x, y, color, opp_color):
    board[x][y] = color
    
    i = 1
    while i <= 8: # checks for open spaces in all 8 squares next to current space
        if i == 1: # path going up
            Pathfind(x, y, 0, -1, color, opp_color)
        elif i == 2: # path going up and right
            Pathfind(x, y, 1, -1, color, opp_color)
        elif i == 3: # path going right
            Pathfind(x, y, 1, 0, color, opp_color)
        elif i == 4: # path going down and right
            Pathfind(x, y, 1, 1, color, opp_color)
        elif i == 5: # path going down
            Pathfind(x, y, 0, 1, color, opp_color)
        elif i == 6: # path going down and left
            Pathfind(x, y, -1, 1, color, opp_color)
        elif i == 7: # path going left
            Pathfind(x, y, -1, 0, color, opp_color)
        elif i == 8: # path going up and left
            Pathfind(x, y, -1, -1, color, opp_color)

        i+=1

def ParseSelection(selection, color, opp_color):
    sel_list = list(selection)
    global m_debug
    global p_debug
    
    if len(sel_list) != 2: # invalid input
        if (len(sel_list) == 3):
            if sel_list[2] == "M": #enable minimax debug
                m_debug = True
            elif sel_list[2] == "P": #pruning debug
                p_debug = True
            else:
                print("Incorrect Debug Character. Correct character is M for minimax or P for alphabeta pruning")
                return False
        else:
            print("Too Many Characters. Please ensure your command is in the format \"A1\"")
            return False
    
    
    # converts format "A1" into format "00" which will be read as indices on the board
    sel_list[0] = ord(sel_list[0]) - 65
    sel_list[1] = ord(sel_list[1]) - 49

    if sel_list[0] > 7 or sel_list[1] > 7:
        print("Invalid command. Please enter a valid board space")
        return False

    if board[sel_list[1]][sel_list[0]] == valid: # the selection is a valid space
        MakeMove(sel_list[1], sel_list[0], color, opp_color)
        return True
    else:
        print("Command is not a valid move. Please select from spaces with a \"" + valid + "\"")
        return False

def CleanValids():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == valid:
                board[i][j] = " "

def CountPoints(color):
    points = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == color:
              points += 1
    return points

def DetermineStrikes(strikes):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == valid: # if there is even 1 valid spot, the game is not over
                return 0
    return strikes + 1 # there are no valid spots

def CanMove():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == valid: # if there is even 1 valid spot, the player can move
                return True
    return False

def Heuristic(color, opp_color):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == color:
                total += 1
                if (i == 0 or i == 7) and (j == 0 or j == 7):
                    total += 4 # corner peice
                elif (i == 0 or i == 7) or (j == 0 or j == 7):
                    total += 2 # side peice
                else:
                    total += 1
    #total = CountPoints(color)-CountPoints(opp_color)
    #PrintBoard()
    #print(total)
                    
    return total

def CopyBoard():
    board_copy = [[" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "]]
    for i in range(len(board)):
        for j in range(len(board[i])):
            board_copy[i][j] = board[i][j]
    return board_copy

def SetBoard(state):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = state[i][j]

def Minimax(color, minormax, depth, alpha, beta): # color, minormax(true for max, false for min), curr ply, maxply

    if color == white: # sets opp color
        opp_color = black
    else:
        opp_color = white

    board_state = CopyBoard()

    if depth == 0: # end of the search, return h
        return Heuristic(color, opp_color), -1, -1
    
    if minormax:
        maxEval = -999999 # large negative number
        max_x = -1
        max_y = -1
        for i in range(len(board_state)):
            for j in range(len(board_state[i])):
                if board_state[i][j] == valid: # loops through valid spaces
                    MakeMove(i, j, color, opp_color) # makes the move through the board
                    CleanValids()                  
                    DeterminePlayableSpaces(opp_color)
                    
                    val, x, y = Minimax(color, False, depth-1, alpha, beta)
        
                    if (m_debug): #output debug values
                        if depth == search_depth: # only prints out possible moves for first search
                            print()
                            print("Possible Move: ", i, j)
                            print("Associated Heuristic: " , val)
                            print()

                    SetBoard(board_state) # resets board to the saved state for next loop
                    if (val > maxEval):
                        max_x = i
                        max_y = j
                    maxEval = max(maxEval, val)
                    alpha = max(alpha, val)
                    if beta <= alpha: # alpha prune

                        if (p_debug):
                            print()
                            print("Alpha Prune at move ",i, j, " where alpha = ", alpha, "and beta = ", beta)
                            print()
                        
                        break
        return maxEval, max_x, max_y
    else:
        minEval = 999999 # large negative number
        min_x = -1
        min_y = -1
        for i in range(len(board_state)):
            for j in range(len(board_state[i])):
                if board_state[i][j] == valid: # loops through valid spaces
                    MakeMove(i, j, opp_color, color) # makes the move through the board
                    CleanValids()                  
                    DeterminePlayableSpaces(color)
                    
                    val, x, y = Minimax(color, True, depth-1, alpha, beta)

                    if (m_debug): #output debug values
                        if depth == search_depth: # only prints out possible moves for first search
                            print()
                            print("Possible Move: ", i, j)
                            print("Associated Heuristic: " , val)
                            print()
        
                    SetBoard(board_state) # resets board to the saved state for next loop
                    #print(val)
                    if (val < minEval):
                        min_x = i
                        min_y = j
                    minEval = min(minEval, val)
                    beta = min(beta, val)
                    if beta <= alpha: # beta prune

                        if (p_debug):
                            print()
                            print("Beta Prune at move ",i, j, " where alpha = ", alpha, "and beta = ", beta)
                            print() 
                        break
        return minEval, min_x, min_y
                    

def OptimalMove(color, opp_color):
    max_h = 0
    x = 0
    y = 0
    board_copy = CopyBoard()
    h, x, y = Minimax(color, True, search_depth, -999999, 999999) # determines heuristic through minimax

    if (m_debug):
        print("Chosen Move: ", x, y)
        print()

    MakeMove(x, y, color, opp_color) # makes move

#----- Main ------
m_debug = False
p_debug = False
while True: # Main Loop
    mode = input("Enter number of players (\"1\" for play vs. AI , \"2\" for 2-player mode): ")

    if mode == "1":
        while True: # Loop for mode 1
            selected_color = input("Please select a color. (\"white\" or \"black\"): ")

            if selected_color == "white":
                current_turn = False # false = white, true = black
                game_over_strikes = 0 # counter used to keep track of how many times there are no available moves, after 2 in a row, game over
                while True:
                    if current_turn == True: # white's turn
                        DeterminePlayableSpaces(white)
                        PrintBoard()
                        game_over_strikes = DetermineStrikes(game_over_strikes)
                        can_move = CanMove()
                        if game_over_strikes >= 2:
                            print("Game Over")
                            break    
                        valid_move = False
                        if can_move:
                            while valid_move == False:
                                selection = input("Please Enter Your Move Below (White): ")
                                valid_move = ParseSelection(selection, white, black)
                                print()
                        CleanValids()
                    else: # black's turn
                        DeterminePlayableSpaces(black)
                        PrintBoard()
                        game_over_strikes = DetermineStrikes(game_over_strikes)
                        can_move = CanMove()
                        if game_over_strikes >= 2:
                            print("Game Over")
                            break
                        valid_move = False
                        if can_move:
                            print("Black's Turn")
                            print()
                            OptimalMove(black, white)
                            m_debug = False
                            p_debug = False
                        CleanValids()
            
                    current_turn = not current_turn
            elif selected_color == "black":
                current_turn = False # false = white, true = black
                game_over_strikes = 0 # counter used to keep track of how many times there are no available moves, after 2 in a row, game over
                while True:
                    if current_turn == True: # white's turn
                        DeterminePlayableSpaces(white)
                        PrintBoard()
                        game_over_strikes = DetermineStrikes(game_over_strikes)
                        can_move = CanMove()
                        if game_over_strikes >= 2: # game over if strikes are exceeded
                            print("Game Over")
                            break    
                        valid_move = False
                        if can_move: # AI makes its move
                            print()
                            print("AI's turn (White)")
                            print()
                            OptimalMove(white, black)
                            m_debug = False
                            p_debug = False
                        CleanValids()
                    else: # black's turn
                        DeterminePlayableSpaces(black)
                        PrintBoard()
                        game_over_strikes = DetermineStrikes(game_over_strikes)
                        can_move = CanMove()
                        if game_over_strikes >= 2:
                            print("Game Over")
                            break
                        valid_move = False
                        if can_move:
                            while valid_move == False:
                                selection = input("Please Enter Your Move Below (Black): ")
                                valid_move = ParseSelection(selection, black, white)
                                print()
                        CleanValids()
            
                    current_turn = not current_turn
            else: # invalid input
                print("Please enter a valid input")
    elif mode == "2":
        current_turn = False # false = white, true = black
        game_over_strikes = 0 # counter used to keep track of how many times there are no available moves, after 2 in a row, game over
        while True:
            if current_turn == True: # white's turn
                DeterminePlayableSpaces(white)
                PrintBoard()
                game_over_strikes = DetermineStrikes(game_over_strikes)
                can_move = CanMove()
                if game_over_strikes >= 2:
                    print("Game Over")
                    break    
                valid_move = False
                if can_move:
                    while valid_move == False:
                        selection = input("Please Enter Your Move Below (White): ")
                        valid_move = ParseSelection(selection, white, black)
                        print()
                CleanValids()
            else: # black's turn
                DeterminePlayableSpaces(black)
                PrintBoard()
                game_over_strikes = DetermineStrikes(game_over_strikes)
                can_move = CanMove()
                if game_over_strikes >= 2:
                    print("Game Over")
                    break
                valid_move = False
                if can_move:
                    while valid_move == False:
                        selection = input("Please Enter Your Move Below (Black): ")
                        valid_move = ParseSelection(selection, black, white)
                        print()
                CleanValids()
    
            current_turn = not current_turn
    else: #invalid input
        print("Please enter valid input")

            


























