def getMaxCalories():
    max = 0
    current_count = 0
    try:
        file = open('input.txt')
        for line in file:
            if line != '\n':
                current_count += int(line)
            else:
                if current_count > max:
                    max = current_count
                current_count = 0
    finally:
        file.close()
    
    print("The most calories an elf has is: " + str(max))

getMaxCalories()