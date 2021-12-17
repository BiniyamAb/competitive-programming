from typing import List

def minSetSize(arr: List[int]) -> int:
    if len(set(arr)) == 1:
            return 1
    
    freqDict, size, sumOf = {}, 0, 0
    
    for i in range(len(arr)):
        freqDict[arr[i]] = freqDict.get(arr[i], 0) + 1
    
    lst = list(freqDict.values())
    lst.sort(reverse=True)
    
    for i in range(len(lst)):
        sumOf+=lst[i]
        size+=1
        
        if sumOf >= len(arr) // 2:
            break
                    
    return size
