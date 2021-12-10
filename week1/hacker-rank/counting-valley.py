import math
def countingValleys(steps, path):
    level = 0
    valleys = 0
    for i in range(steps):
        if path[i] == "D":
            if level == 0:
                valleys+=1
            level += -1
        elif path[i] == "U":
            level += 1
    return valleys
        

print(countingValleys(8, "UDDDUDUU"))