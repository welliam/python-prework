from random import randint
from collections import namedtuple


def print_board(board):
    for row in board:
        print " ".join(row)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


point = namedtuple('Point', ['row', 'col'])


def random_point(board):
    return point(random_row(board), random_col(board))


def get_int(prompt):
    while True:
        try:
            return int(raw_input(prompt))
        except TypeError:
            print "That's not a number!"


def read_point():
    return point(get_int('Guess row: '), get_int('Guess column: '))


def point_ref(board, point):
    return board[point.row][point.col]


def point_set(board, point, to):
    board[point.row][point.col] = to


def point_in_range(board, point):
    row, col = point
    return row >= 0 and col >= 0 and \
        row < len(board) and col < len(board[0])


def turn(board, battleship, turn_count):
    guess = read_point()
    if guess == battleship:
        print 'Congratulations! You sunk my battleship!'
        return False
    elif not point_in_range(board, guess):
        print "Oops, that's not even in the ocean."
    elif point_ref(board, guess) == 'X':
        print 'You guessed that one already.'
    else:
        print 'You missed my battleship!'
        point_set(board, guess, 'X')
    return True


def report_game_over(board, battleship):
    point_set(board, battleship, '*')
    print 'Game over! My battleship is at the *:'
    print_board(board)


def run_game(board, battleship, turns):
    print "Let's play Battleship!"

    for turn_count in range(turns):
        print 'Turn', turn_count + 1, 'of', turns
        print_board(board)
        if not turn(board, battleship, turn_count):
            return
        print

    report_game_over(board, battleship)


def game(size, turns):
    board = []
    for x in range(size):
        board.append(["O"] * size)
    battleship = random_point(board)
    run_game(board, battleship, turns)


game(5, 5)
