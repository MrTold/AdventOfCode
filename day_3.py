# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
#
# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.
#
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
#
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:
#
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
#
# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
#
# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
#
# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
#
# So, the gamma rate is the binary number 10110, or 22 in decimal.
#
# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
#
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
from functools import reduce
import numpy as np

input_file = open("input_3d.txt", "r")
lines = input_file.read().split("\n")
counter = []
n_lines = len(lines)

for i in range(len(lines[0])):
    counter.append(0)

ar = []

for line in lines:
    ar.append(np.array([int(char) for char in line]))

counter = np.array(ar).sum(axis=0)
print(counter)

gamma = ''
epsilon = ''

for x in counter:
    if x > n_lines / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma, epsilon)
print(int(gamma, 2) * int(epsilon, 2))

def most_common(arr, i):
    count = 0
    for x in arr:
        if x[i] == '1':
            count += 1
    return '1' if count >= len(arr)/2 else '0'

def least_common(arr, i):
    count = 0
    for x in arr:
        if x[i] == '1':
            count += 1
    return '1' if count < len(arr)/2 and count != 0 else '0'

def ox(arr, i):
    if len(arr) > 1:
        new_arr = []
        for x in arr:
            if x[i] == most_common(arr, i):
                new_arr.append(x)
        print(new_arr)
        return ox(new_arr, i+1)
    else:
        return arr[0]


def co2(arr, i):
    if len(arr) > 1:
        new_arr = []
        for x in arr:
            if x[i] == least_common(arr, i):
                new_arr.append(x)
        print(new_arr)
        return co2(new_arr, i+1)
    else:
        return arr[0]


ox_level = ox(lines, 0)
co2_level = co2(lines, 0)
print(ox_level)
print(co2_level)

print(int(ox_level, 2) * int(co2_level, 2))