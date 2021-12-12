import math
def solution():
    inputs = input()
    inputs = inputs.split(" ")
    m, n, a = int(inputs[0]), int(inputs[1]), int(inputs[2])

    leastm = math.ceil(m / a)
    leastn = math.ceil(n / a)

    least2 = leastm * leastn

    print(least2)

solution()