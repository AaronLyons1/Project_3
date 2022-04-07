from random import randint

hidden_board = [{' '} * 8 for x in range(8)]
player_board = [{' '} * 8 for x in range(8)]

letters_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def start_board(board):
    """
    This function will lay out the board and make it visible
    """
    print('A B C D E F G H')
    print('  ')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def ships():
    """
    This function will make the ships
    """
    for ship in range(5):
         ship_x, ship_y = randint(0,7), randint(0,7)

    while board[ship_x][ship_y] == "X":
        ship_x, ship_y = randint(0,7), randint(0,7)

    board[ship_x][ship_y] = 'X'

def where_is_ship():
    """
    This will ask the player for thier inputs and input them
    """
    y_axis = input("Enter a number ranging from 1-8: ")
    if y_axis not in '12345678':
        print('Invalid, Please enter a valid row number')
    else:
        y_axis = input("Enter a number ranging from 1-8: ")

    x_axis = input("Enter a letter ranging from A-H: ")
    if x_axis not in 'ABCDEFGH':
         print('Invalid, Please enter a valid letter')
    else:
        x_axis = input("Enter a letter ranging from A-H: ")
         
    return int(y_axis) -1, letters_numbers(x_axis) #Reason for -1 is because its technically 1 on the board but its 0 in our list

def hit_ship():
    """
    This function will recognise if a ship was hit
    """
    pass


ships()

turns = 10
while turns > 0:
    pass
