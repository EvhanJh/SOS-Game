""" Tests """


def test_s(board):
    """
    Test S
    :param board: Board
    :type board: list
    """
    board[2][3] = 2
    board[4][3] = 2
    board[3][2] = 2
    board[3][4] = 2
    board[3][1] = 1
    board[1][3] = 1
    board[5][3] = 1
    board[3][5] = 1

    board[2][2] = 2
    board[4][2] = 2
    board[2][4] = 2
    board[4][4] = 2
    board[1][1] = 1
    board[1][5] = 1
    board[5][1] = 1
    board[5][5] = 1


def test_o(board):
    """
    Test O
    :param board: Board
    :type board: list
    """
    board[2][3] = 1
    board[2][4] = 1
    board[3][4] = 1
    board[4][4] = 1
    board[4][3] = 1
    board[4][2] = 1
    board[3][2] = 1
    board[2][2] = 1
