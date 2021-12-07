input_file = open("input_7d.txt", "r")
crabs = [int(x) for x in input_file.read().strip().split(',')]

#part one
min_fuel = 10000000000
for i in range(max(crabs)):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - i)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)

#part two
min_fuel = 10000000000
for i in range(max(crabs)):
    fuel = 0
    for crab in crabs:
        fuel += (abs(crab - i) * (abs(crab - i) + 1)) / 2       #for Gauss: sum of i for i going from 1 to n = n(n+1) / 2
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)

