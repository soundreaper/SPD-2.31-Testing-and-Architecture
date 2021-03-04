# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

import random

# Global constant for board size since
BOARD_SIZE = 10


def drawBoard(board):
    """
    This function prints out the board that it was passed.
    """

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    """
    Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    """

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    """ 
    Randomly choose the player who goes first.
    """

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    """
    This function returns True if the player wants to play again, otherwise it returns False.
    """

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    """
    Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much.
    """

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    """
    Make a duplicate of the board list and return it the duplicate.
    """

    return board.copy()


def isSpaceFree(board, move):
    """
    Return true if the passed move is free on the passed board.
    """

    return board[move] == ' '


def getPlayerMove(board):
    """
    Let the player type in their move.
    """

    player_input = ' '
    while player_input not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(player_input)):
        print('What is your next move? (1-9)')
        player_input = input()
    return int(player_input)


def chooseRandomMoveFromList(board, movesList):
    """
    Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move.
    """

    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves:
        return random.choice(possibleMoves)
    return None


def getComputerMove(board, letter):
    """
    Given a board and the computer's letter, determine where to move and return that move.
    """

    player = letter[0]
    comp = letter[1]

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, comp, i)
            if isWinner(copy, comp):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, player, i)
            if isWinner(copy, player):
                return i

    # Try to take one of the corners, if they are free.
    try_move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if try_move is not None:
        return try_move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    """
    Return True if every space on the board has been taken. Otherwise return False.
    """

    for i in range(1, BOARD_SIZE):
        if isSpaceFree(board, i):
            return False
    return True


def gameStart(order, letters):
    """
    Creating the game board with given turn order and what letter each participant has.
    """

    # Reset the board
    theBoard = [' '] * BOARD_SIZE

    if order == 'player':
        curr = 0
    else:
        curr = 1

    while True:
        if curr == 0:
            move = getPlayerMove(theBoard)
        else:
            move = getComputerMove(theBoard, letters)

        makeMove(theBoard, letters[curr], move)

        if curr == 1:
            drawBoard(theBoard)

        if isWinner(theBoard, letters[curr]):
            if curr == 0:
                print('Hooray! You have won the game!')
            break

        if isBoardFull(theBoard):
            print('The game is a tie!')
            break

        curr ^= 1


def initializeGame():
    """
    Game Prompt shown in terminal and where particpant turn order and letter are decided.
    """

    print('Welcome to Tic Tac Toe!')

    while True:

        givenLetters = inputPlayerLetter()

        startingPlayer = whoGoesFirst()
        print(startingPlayer + "goes first!")

        gameStart(startingPlayer, givenLetters)

        if not playAgain():
            break


if __name__ == "__main__":
    initializeGame()
