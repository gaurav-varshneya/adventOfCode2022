def countFullyContained():
    fullyContainedCount = 0
    try:
        file = open('input.txt')
        for line in file:
            line = line.strip()
            line_arr = line.split(',')
            elf_one = [int(x) for x in line_arr[0].split('-')]
            elf_two = [int(x) for x in line_arr[1].split('-')]

            if ((elf_one[0] >= elf_two[0] and elf_one[1] <= elf_two[1]) or
                (elf_two[0] >= elf_one[0] and elf_two[1] <= elf_one[1])):
                fullyContainedCount += 1
    finally:
        file.close()

    print("Fully contained shifts: " + str(fullyContainedCount))

countFullyContained()