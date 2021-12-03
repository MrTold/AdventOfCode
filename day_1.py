input_file = open("input_1d.txt", "r")
l = []
n = input_file.read().split("\n")
for x in n:
    l.append(int(x))

n_increase = 0
for i in range(1, len(l)):
    if l[i-1] < l[i]:
        n_increase += 1

print(n_increase)

l_triple = []
for i in range(len(n) - 2):
    l_triple.append(int(n[i]) + int(n[i+1]) + int(n[i+2]))

n_increase = 0
for i in range(1, len(l_triple)):
    if l_triple[i-1] < l_triple[i]:
        n_increase += 1

print(n_increase)