import numpy as np

input_file = open("input_5d.txt", "r")
lines = [[[int(x) for x in coords.split(',')] for coords in line.split(' -> ')] for line in input_file.read().strip().split('\n')]
maximum = max([max([max(x) for x in line]) for line in lines])
field = np.zeros((maximum + 1, maximum + 1))

lines = list(map(lambda line: {'x1': line[0][0], 'y1': line[0][1], 'x2': line[1][0], 'y2': line[1][1]}, lines))

#part one
for line in lines:
    if line['x1'] == line['x2']:        #x coordinate is equal
        for i in range(abs(line['y2']-line['y1']) + 1):
            field[min(line['y1'], line['y2']) + i][line['x1']] += 1
    elif line['y1'] == line['y2']:      #y coordinate is equal
        for i in range(abs(line['x2']-line['x1']) + 1):
            field[line['y1']][min(line['x1'], line['x2']) + i] += 1

counter = 0
for row in field:
    counter += len(list(filter(lambda x: x > 1, row)))  #number of elements grater than one in a row

print(f'Solution part one: {counter}')

#part two
for line in lines:
    if line['x1'] != line['x2'] and line['y1'] != line['y2']:   #it is a diagonal
        for i in range(abs(line['y2']-line['y1']) + 1):
            if line['y1'] < line['y2'] and line['x1'] < line['x2'] or line['y1'] > line['y2'] and line['x1'] > line['x2']:      #diagonal from top left to bottom right
                field[min(line['y1'], line['y2']) + i][min(line['x1'], line['x2']) + i] += 1
            else:                                                                                                               #diagonal from bottom left to top right
                field[max(line['y1'], line['y2']) - i][min(line['x1'], line['x2']) + i] += 1

counter = 0
for row in field:
    counter += len(list(filter(lambda x: x > 1, row)))  #number of elements grater than one in a row

print(f'Solution part two: {counter}')