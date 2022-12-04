def getScore():
    running_count = 0
    score_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    move_dict = {
        'X': 'A', # rock
        'Y': 'B', # paper
        'Z': 'C'  # scissors
    }
    try:
        file = open('input.txt')
        for line in file:
            arr = line.split()
            opp = arr[0]
            me = move_dict[arr[1]]

            move_score = score_dict[arr[1]]
            running_count += move_score

            # opp chooses rock
            if (opp == me): # it's a tie
                running_count += 3 
            elif ((opp == 'A' and me == 'B') or
                  (opp == 'B' and me == 'C') or
                  (opp == 'C' and me == 'A')):
                running_count += 6

    finally:
        file.close()
    
    print("My score will be: " + str(running_count))

getScore()
