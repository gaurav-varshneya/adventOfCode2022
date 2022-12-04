def getPrioritySum():
    priority_sum = 0
    try:
        file = open('input.txt')
        for line in file:
            line = line.strip()
            first_half, second_half = line[:len(line)//2],  line[len(line)//2:]
            first_half_set = set(first_half)
            second_half_set = set(second_half)

            intersection = first_half_set & second_half_set

            for dup in intersection:
                if dup.isupper():
                    priority_sum += ord(dup) - 38
                else:
                    priority_sum += ord(dup) - 96
    finally:
        file.close()

    print('The priority sum is: ' + str(priority_sum))

getPrioritySum()