""" Algorithms """

from random import randint
import json


def new_board(number):
    """
    Create the board
    :param number: Number of lines / columns
    :type number: int
    :return: board
    """
    return [[0] * number for iterator in range(number)]


def display(board, number):
    """
    Display the board
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    """
    coords = 0
    for i in range(0, 5):
        print('\n')
    print('   ', end='')
    for i in range(0, number):
        print('  ', i, end='')
    print('\n\n')
    for line in board:
        print(coords, '   ', end='')
        coords += 1
        for case in line:
            if case == 0:
                case = '·'
            elif case == 1:
                case = 'S'
            else:
                case = 'O'
            print('', case, ' ', end='')
        print('\n')


def possible_square(board, number, i, j):
    """
    Check if coordinates
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :param i: Coordinate x
    :type i: int
    :param j: Coordinate y
    :type j: int
    :return: bool
    """
    if in_board(number, i, j):
        if board[i][j] == 0:
            return 1
    return 0


def in_board(number, i, j):
    """
    Check if coordinates are in board
    :param number: Number of lines / columns
    :type number: int
    :param i: Coordinate x
    :type i: int
    :param j: Coordinate y
    :type j: int
    :return: bool
    """
    if 0 > i > number - 1:
        if 0 > j > number - 1:
            return 0
    return 1


def has_letter(board, i, j):
    """
    Check if a letter is setted
    :param board: Board
    :type board: list
    :param i: Coordinate x
    :type i: int
    :param j: Coordinate y
    :type j: int
    :return: bool
    """
    if board[i][j] == 0:
        return 0
    return 1


def select_coordinates(number):
    """
    Ask coordinates to users
    :param number: Number of lines / columns
    :type number: int
    :return: int
    """
    i = input('Choisissez une coordonnée verticale » ')
    while not i.isdigit() or int(i) < 0 or int(i) > number - 1:
        i = input('Choisissez une coordonnée verticale » ')

    j = input('Choisissez une coordonnée horizontale » ')
    while not j.isdigit() or int(j) < 0 or int(j) > number - 1:
        j = input('Choisissez une coordonnée horizontale » ')

    return int(j), int(i)


def select_letter():
    """
    Ask letter to users
    :return: str
    """
    letters = ['S', 's', 'O', 'o', '0']
    letter = input('Choisissez une lettre [S | O] » ')
    while letter not in letters:
        letter = input('Choisissez une lettre [S | O] » ')

    return letter


def update(board, number, i, j, letter, scores, player, lines, players_count):
    """
    Update the board
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :param i: Coordinate y
    :type i: int
    :param j: Coordinate x
    :type j: int
    :param letter: Action letter
    :type letter: int
    :param scores: Users points
    :type scores: list
    :param player: Player ID
    :type player: int
    :param lines: Extreme coordinates of lines
    :type lines: list
    :param players_count: Count of players
    :type players_count: int
    """
    print(i, j)
    if letter == 1:
        update_score_s(board, number, i, j, scores, player, lines)
    else:
        update_score_o(board, number, i, j, scores, player, lines)

    board[i][j] = letter

    display(board, number)

    for iterator in range(0, players_count):
        print('Joueur ' + str(iterator + 1) + ' » ' + str(scores[iterator]) + ' points')
    print('\nTour » Joueur', player + 1, '\n')


def update_score_s(board, number, i, j, scores, player, lines):
    """
    Check SOS words around to S
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :param i: Coordinate x
    :type i: int
    :param j: Coordinate y
    :type j: int
    :param scores: Users points
    :type scores: list
    :param player: Player ID
    :type player: int
    :param lines: Extreme coordinates of lines
    :type lines: list
    """
    if i + 1 < number and j - 1 >= 0:
        if board[i + 1][j - 1] == 2:
            if i + 2 < number and j - 2 >= 0:
                if board[i + 2][j - 2] == 1:
                    # print('Diagonale haut / ')
                    lines.append([(i, j), (i + 2, j - 2), int(player)])
                    scores[player] += 1

    if j - 1 >= 0:
        if board[i][j - 1] == 2:
            if j - 2 >= 0:
                if board[i][j - 2] == 1:
                    # print('Horizontal droite')
                    lines.append([(i, j), (i, j - 2), int(player)])
                    scores[player] += 1

    if j + 1 < number:
        if board[i][j + 1] == 2:
            if j + 2 < number:
                if board[i][j + 2] == 1:
                    # print('Horizontal gauche')
                    lines.append([(i, j), (i, j + 2), int(player)])
                    scores[player] += 1

    if i - 1 >= 0 and j + 1 < number:
        if board[i - 1][j + 1] == 2:
            if i - 2 >= 0 and j + 2 < number:
                if board[i - 2][j + 2] == 1:
                    # print('Diagonale bas / ')
                    lines.append([(i, j), (i - 2, j + 2), int(player)])
                    scores[player] += 1

    if i + 1 < number and j + 1 < number:
        if board[i + 1][j + 1] == 2:
            if i + 2 < number and j + 2 < number:
                if board[i + 2][j + 2] == 1:
                    # print('Diagonale haut \ ')
                    lines.append([(i, j), (i + 2, j + 2), int(player)])
                    scores[player] += 1

    if i - 1 >= 0 and j - 1 >= 0:
        if board[i - 1][j - 1] == 2:
            if i - 2 >= 0 and j - 2 >= 0:
                if board[i - 2][j - 2] == 1:
                    # print('Diagonale bas \ ')
                    lines.append([(i, j), (i - 2, j - 2), int(player)])
                    scores[player] += 1

    if i + 1 < number:
        if board[i + 1][j] == 2:
            if i + 2 < number:
                if board[i + 2][j] == 1:
                    # print('Vertical haut')
                    lines.append([(i, j), (i + 2, j), int(player)])
                    scores[player] += 1

    if i - 1 >= 0:
        if board[i - 1][j] == 2:
            if i - 2 >= 0:
                if board[i - 2][j] == 1:
                    # print('Vertical bas')
                    lines.append([(i, j), (i - 2, j), int(player)])
                    scores[player] += 1


def update_score_o(board, number, i, j, scores, player, lines):
    """
    Check SOS words around to O
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :param i: Coordinate x
    :type i: int
    :param j: Coordinate y
    :type j: int
    :param scores: Users points
    :type scores: list
    :param player: Player ID
    :type player: int
    :param lines: Extreme coordinates of lines
    :type lines: list
    """
    if number - 1 > i > 0:
        if board[i][j] == 0 and board[i - 1][j] == 1 and board[i + 1][j] == 1:
            # print('Vertical')
            lines.append([(i - 1, j), (i + 1, j), int(player)])
            scores[player] += 1
    if number - 1 > j > 0:
        if board[i][j] == 0 and board[i][j - 1] == 1 and board[i][j + 1] == 1:
            # print('Horizontal')
            lines.append([(i, j - 1), (i, j + 1), int(player)])
            scores[player] += 1
    if number - 1 > j > 0 and number - 1 > i > 0:
        if board[i][j] == 0 and board[i - 1][j - 1] == 1 and board[i + 1][j + 1] == 1:
            # print('Diagonale \ ')
            lines.append([(i - 1, j - 1), (i + 1, j + 1), int(player)])
            scores[player] += 1
        if board[i][j] == 0 and board[i - 1][j + 1] == 1 and board[i + 1][j - 1] == 1:
            # print('Diagonale / ')
            lines.append([(i - 1, j + 1), (i + 1, j - 1), int(player)])
            scores[player] += 1


def has_winner(board, number):
    """
    Check if has winner
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :return: str
    """
    for i in range(0, number):
        for j in range(0, number):
            if board[i][j] == 0:
                return 0
    return 1


def random_ai(board, number, scores, player, lines, players_count):
    """
    Artificial Intelligence with random
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :param scores: Users points
    :type scores: list
    :param player: Player ID
    :type player: int
    :param lines: Extreme coordinates of lines
    :type lines: list
    :param players_count: Count of players
    :type players_count: int
    """
    x_coord = randint(0, number - 1)
    y_coord = randint(0, number - 1)
    s_type = randint(1, 2)
    while has_letter(board, x_coord, y_coord):
        x_coord = randint(0, number - 1)
        y_coord = randint(0, number - 1)
        s_type = randint(1, 2)
    update(board, number, x_coord, y_coord, s_type, scores, player, lines, players_count)


def create_save(board, number, scores, player, lines, players_count, artificial_intelligence):
    """
    Create the game save
    """
    file = open('save.json', 'w+')
    data = {
        'number': number,
        'players_count': players_count,
        'player': player,
        'artificial_intelligence': artificial_intelligence,
        'scores': scores,
        'board': board,
        'lines': lines
    }
    file.write(json.dumps(data))
    file.close()


def load_save():
    """
    Load the game save
    """
    with open('save.json') as json_data:
        data = json.load(json_data)
    return data
