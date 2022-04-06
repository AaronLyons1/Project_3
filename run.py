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

def ship():
    """
    This function will make the ships
    """
    pass

def where_is_ship():
    """
    This will ask the player for thier inputs and input them
    """
    pass

def hit_ship():
    """
    This function will recognise if a ship was hit
    """
    pass


ship()

turns = 10
while turns > 0:
    pass
