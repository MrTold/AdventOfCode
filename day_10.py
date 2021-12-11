input_file = open('input_10d.txt', 'r')
lines = [line for line in input_file.read().strip().split('\n')]

open_par = ['(', '[', '{', '<']
close_par = [')', ']', '}', '>']

# part one
error_val = [3, 57, 1197, 25137]
error_lines = []
er_tot = 0
for line in lines:
    expected = []
    for x in line:
        if x in open_par:
            expected.append(close_par[open_par.index(x)])
        else:
            if x != expected[-1]:
                error_lines.append(line)
                er_tot += error_val[close_par.index(x)]
                break
            else:
                expected.pop()

print(f"Solution part one: {er_tot}")


# part two
incomplete_l = lines[:]
inc_expected = []
for line in lines:
    expected = []
    inc = True
    for x in line:
        if inc:
            if x in open_par:
                expected.append(close_par[open_par.index(x)])
            else:
                if x != expected[-1]:
                    incomplete_l.remove(line)
                    inc = False
                else:
                    expected.pop()
    if inc:
        inc_expected.append(reversed(expected))

scores = []
for ex in inc_expected:
    score = 0
    for x in ex:
        score *= 5
        score += 1 + close_par.index(x)
    scores.append(score)

scores.sort()
print(f"Solution part one: {scores[int(len(scores) / 2)]}")
