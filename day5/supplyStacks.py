instruction_start = 0
input_file = 'input.txt'

def execute():
    stacks = parseInput()
    start = False
    try:
        file = open(input_file)
        for idx, line in enumerate(file):
            if (idx == instruction_start):
                start = True
            if start:
                move_row = [int(s) for s in line.split() if s.isdigit()] # how many, from, to
                print('THE MOVE: ' + str(move_row))
                for x in range(move_row[0]):
                    stacks[move_row[2] - 1].append(stacks[move_row[1] - 1].pop())
                printStacks(stacks)
    finally:
        file.close

    # get top row
    top_row = ''
    for stack in stacks:
        top = ''
        while top == '':
            top = stack.pop()

        top_row += top
    printStacks(stacks)
    print('THE TOP ROW: ' + top_row)

def printArr(arr):
    print('\n'.join(arr))

def printStacks(stacks):
    for stack in stacks:
        print(stack)
        print('\n')

def parseInput():
    input_picture = []
    try:
        file = open(input_file)
        for idx, line in enumerate(file):
            if not line.strip():
                global instruction_start
                instruction_start = idx + 1
                break
            input_picture.append(line)
    finally:
        file.close()
    print("THE INPUT")
    printArr(input_picture)
    print("INPUT DONE")
    stacks = []
    num_of_stacks = len(input_picture.pop().split())
    print(num_of_stacks)

    for x in range(num_of_stacks):
        stacks.append([])

    while input_picture:
        row = input_picture.pop().replace('[', ' ').replace(']', ' ')
        row = [row[i : i + 4].strip() for i in range(0, len(row), 4)]
        for idx, char in enumerate(row):
            if char != '':
                stacks[idx].append(char)

    print('THE STACKS BEFORE')
    print(stacks)
    return stacks

execute()