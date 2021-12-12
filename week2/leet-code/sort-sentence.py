def sortSentence(s):
    arr = s.split(" ")
    lst = []
    final = []
    for i in range(len(arr)):
        lst.append(int(arr[i][-1]))

    lst.sort()

    for num in lst:
        for j in range(len(arr)):
            if num == int(arr[j][-1]):
                final.append(arr[j][:-1])


    str1 = ""
    for ele in final: 
        str1 += ele + " "

    return str1[:-1]
