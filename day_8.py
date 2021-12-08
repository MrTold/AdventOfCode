#all segments of 4 and 7 are contained in 9 and the there is only one segment of 9 not contained in 4 a nd 7
def find_9(x, dig_4):
    dig_4_set = set(list(dig_4))
    try_dig = set(list(x))
    if dig_4_set.issubset(try_dig):
        return True


def find_3(x, dig_7, ):
    dig_7_set = set(list(dig_7))
    try_dig = set(list(x))
    if dig_7_set.issubset(try_dig):
        return True


def find_0(x, dig_4, dig_7):
    dig_4_set = set(list(dig_4))
    dig_7_set = set(list(dig_7))
    try_dig = set(list(x))
    if dig_7_set.issubset(try_dig) and not dig_4_set.issubset(try_dig):
        return True


def find_6(x, dig_4, dig_7):
    dig_4_set = set(list(dig_4))
    dig_7_set = set(list(dig_7))
    try_dig = set(list(x))
    if not dig_7_set.issubset(try_dig) and not dig_4_set.issubset(try_dig):
        return True


def find_5(x, dig_3, dig_4):
    dig_3_set = set(list(dig_3))
    dig_4_set = set(list(dig_4))
    try_dig = set(list(x))
    unique_segment = try_dig - dig_3_set
    if len(unique_segment) == 1 and unique_segment.issubset(dig_4_set):
        return True

def find_2(x, dig_3, dig_4):
    dig_3_set = set(list(dig_3))
    dig_4_set = set(list(dig_4))
    try_dig = set(list(x))
    unique_segment = try_dig - dig_3_set
    if len(unique_segment) == 1 and not unique_segment.issubset(dig_4_set):
        return True

def main():
    input_file = open('input_8d.txt', 'r')
    lines = input_file.read().strip().split('\n')
    inputs = [line.split(' | ')[0].split(' ') for line in lines]
    outputs = [line.split(' | ')[1].split(' ') for line in lines]

    #part one
    counter = 0
    for out in outputs:
        for digit in out:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                counter += 1

    print(f'Solution part one: {counter}')

    #part two
    sum_out = 0
    for i in range(len(lines)):
        inp = inputs[i]
        digits = [''] * 10
        digits[1] = list(filter(lambda x: len(x) == 2, inp))[0]
        digits[4] = list(filter(lambda x: len(x) == 4, inp))[0]
        digits[7] = list(filter(lambda x: len(x) == 3, inp))[0]
        digits[8] = list(filter(lambda x: len(x) == 7, inp))[0]
        digits[0] = list(filter(lambda x: find_0(x, digits[4], digits[7]) and len(x) == 6, inp))[0]
        digits[3] = list(filter(lambda x: find_3(x, digits[7]) and len(x) == 5, inp))[0]
        digits[5] = list(filter(lambda x: find_5(x, digits[3], digits[4]) and len(x) == 5, inp))[0]
        digits[6] = list(filter(lambda x: find_6(x, digits[4], digits[7]) and len(x) == 6, inp))[0]
        digits[9] = list(filter(lambda x: find_9(x, digits[4]) and len(x) == 6, inp))[0]
        digits[2] = list(filter(lambda x: find_2(x, digits[3], digits[4]) and len(x) == 5, inp))[0]

        number_out = ''
        for digit in outputs[i]:
            for i in range(len(digits)):
                if set(list(digits[i])) == set(list(digit)):
                    number_out += str(i)
        sum_out += int(number_out)

    print(f'Solution part two: {sum_out}')

main()