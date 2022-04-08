from random import randint

hidden_board = [[" "] * 6 for x in range(6)]
player_board = [[" "] * 6 for x in range(6)]

letters_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,}

def start_board(board):
    """
    This function will lay out the board and make it visible
    """
    print("  A B C D E F")
    print("  +-+-+-+-+-+")
    row_num = 1
    for x_axis in board:
        print("%d|%s|" % (row_num, "|".join(x_axis)))
        row_num += 1

def ships(board):
    """
    This function will make the ships
    """
    for ship in range(5):
        ship_y, ship_x = randint(0, 5), randint(0, 5)
        while board[ship_y][ship_x] == "X":
            ship_y, ship_x = randint(0, 5), randint(0, 5)

    board[ship_y][ship_x] = 'X'

def where_is_ship():
    """
    This will ask the player for thier inputs and input them
    """
    y_axis = int(input("Enter a number ranging from 1-8: "))
    if (0 >= y_axis >= 8):
        y_axis = int(input("Enter a number ranging from 1-8: "))
        0 >= y_axis >= 8
    else:
        print('ERROR, Please enter a valid row number')
        y_axis = int(input("Enter a number ranging from 1-8: "))
        if (0 >= y_axis >= 8):
            y_axis = int(input("Enter a number ranging from 1-8: "))
            0 >= y_axis >= 8
        else:
            print('ERROR, Please enter a valid row number')
            y_axis = int(input("Enter a number ranging from 1-8: "))
            if (0 >= y_axis >= 8):
                y_axis = int(input("Enter a number ranging from 1-8: "))
                0 >= y_axis >= 8
            else:
                print('ERROR, Please enter a valid row number')
                y_axis = int(input("Enter a number ranging from 1-8: "))

    x_axis = input("Enter a letter ranging from A-H: ").upper()
    while x_axis not in 'ABCDEFGH':
        print('Invalid, Please enter a valid letter')
        x_axis = input("Enter a letter ranging from A-H: ").upper()

    return int(y_axis) -1, letters_numbers[x_axis]
    

def hit_ship(board):
    """
    This function will recognise if a ship was hit
    """
    score = 0
    for y_axis in board:
        for x_axis in y_axis:
            if x_axis == "X":
                score += 1
    return score

if __name__ == "__main__": #This line is used to allow or prevent parts of code from being run when the modules are imported           
    ships(hidden_board)
    turns = 10
    while turns > 0:
        print("Where do you think the ships are?")
        start_board(player_board)
        y_axis, x_axis = where_is_ship()
        if player_board[y_axis][x_axis] == "0":
            print("You have already hit that location")
        elif hidden_board[y_axis][x_axis] == "X":
            print("Hit")
            player_board[y_axis][x_axis] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            player_board[y_axis][x_axis] = "0"   
            turns -= 1     
        if hit_ship(player_board) == 5:
            print("You Win")
            break
        print(f"You have {turns} turns left")
        if turns == 0:
            print("Sorry you have run out of tries")


#python3 run.py