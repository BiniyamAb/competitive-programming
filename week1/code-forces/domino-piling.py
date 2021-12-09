def solution():
    a = input()
    a = a.split(" ")
    m, n = int(a[0]), int(a[1])

    result = (m * n) // 2

    print(result)