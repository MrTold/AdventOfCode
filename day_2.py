input_file = open("input_2d.txt", "r")
depth = 0
position = 0
lines = input_file.read().split("\n")

for command in lines:
    t = command.split(" ")
    if t[0] == "forward":
        position += int(t[1])
    elif t[0] == "down":
        depth += int(t[1])
    elif t[0] == "up":
        depth -= int(t[1])

print(depth * position)

aim = 0
position = 0
depth = 0
for command in lines:
    t = command.split(" ")
    if t[0] == "forward":
        position += int(t[1])
        depth += aim * int(t[1])
    elif t[0] == "down":
        aim += int(t[1])
    elif t[0] == "up":
        aim -= int(t[1])

print(depth * position)