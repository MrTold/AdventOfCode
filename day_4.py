import numpy as np

def check_board(board):
    flipped_board = board.T     #swaps the rows and columns of the board
    row_check, column_check = False, False
    for i in range(5):
        row_check = True if len(list(filter(lambda x: x['pkd'], board[i]))) == 5 else column_check                 #true if a row is completly checked
        column_check = True if len(list(filter(lambda x: x['pkd'], flipped_board[i]))) == 5 else row_check         #true if a column is completly checked
    return row_check or column_check


def get_result(board, number):
    unmarked_sum = 0
    for row in board:
        for n  in row:
            if n['pkd'] == 0:
                unmarked_sum += n['num']
    return unmarked_sum * number


#code for solving part one
def part_1(random_numbers, boards):
    for number in random_numbers:
        for board in boards:
            # mark picked number in board
            for row in board:
                for n in row:
                    if n['num'] == number:
                        n['pkd'] = 1

            if check_board(board):
                return get_result(board, number)


#code for solving part two
def part_2(random_numbers, boards):
    win_boards = [False] * len(boards)
    last_result = 0
    for number in random_numbers:
        for i in range(len(boards)):
            # mark picked number in board
            for row in boards[i]:
                for n in row:
                    if n['num'] == number:
                        n['pkd'] = 1

            if check_board(boards[i]):
                if not win_boards[i]:
                    last_result = get_result(boards[i], number)
                win_boards[i] = True
    return last_result


def main():
    input_file = open("input_4d.txt", "r")

    #input formatting
    random_numbers = [int(x) for x in input_file.readline().split(',')]
    lines = input_file.read().strip().split("\n")
    rows = [[{'num': int(x), 'pkd': 0} for x in list(filter(None, row.strip().split(' ')))] for row in lines]
    boards = []
    for i in range(int((len(rows)+1)/6)):
        boards.append(np.array([rows[i*6], rows[i*6 + 1], rows[i*6 + 2], rows[i*6 + 3], rows[i*6 + 4]]))

    print(f'Solution part one: {part_1(random_numbers, boards)}')
    print(f'Solution part two: {part_2(random_numbers, boards)}')


main()