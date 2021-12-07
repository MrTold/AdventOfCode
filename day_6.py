N_DAYS = 256

input_file = open("input_6d.txt", "r")
initial_state = [int(x) for x in input_file.read().strip().split(',')]
print(initial_state)


fish_by_day_left = [0] * N_DAYS  # indices are shifted by 1 with respect to the actual number of days left
for i in range(N_DAYS):  # compute the total fish generated by one fish at state 0 for all days
    fish_list = [0]
    generated_fish = 0  # fish generated by fish with already known values
    for j in range(i, -1, -1):  # loops from the current day(j) to the end
        fish_list_copy = []  # use a copy of the list to avoid problems with indices when removing fish
        for k in range(len(fish_list)):
            if fish_list[k] > 0:  # update current fish
                fish_list_copy.append(fish_list[k] - 1)
            else:
                if fish_by_day_left[j] == 0:  # resets current fish and adds a new one
                    fish_list_copy.append(6)
                    fish_list_copy.append(8)
                else:  # if the number of fish generated at that day have already been computed it uses that value and removes the fish (Don't add it to the copy list)
                    generated_fish += fish_by_day_left[j]
        fish_list = fish_list_copy[:]

    fish_by_day_left[i] = generated_fish + len(fish_list)

print(fish_by_day_left)

#part one
days = 80
total_fish = 0
for fish in initial_state:
    total_fish += fish_by_day_left[days - 1 - fish]

print(f'Solution part one: {total_fish}')

#part two
days = 256
total_fish = 0
for fish in initial_state:
    total_fish += fish_by_day_left[days - 1 - fish]

print(f'Solution part one: {total_fish}')
