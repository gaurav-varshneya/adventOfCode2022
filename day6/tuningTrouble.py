input_file = 'input.txt'

def tuningTrouble():
    try:
        file = open(input_file)
        for line in file:
            findMarker(line, 4)
            findMarker(line, 14)
            
    finally:
        file.close()

# k is the number of distinct characters that you want
def findMarker(data, k):

    for i in range(len(data) - 1):
        end = k + i
        sub_arr = data[0 + i : end]
        dup_set = set(sub_arr)
        if len(dup_set) == k: 
            print('Number of characters that need to be processed for ' + str(k) + ' distinct: ' + str(end))
            return


tuningTrouble()