from typing import List

def findOriginalArray(changed: List[int]) -> List[int]:
    freqDict = {}
    changed.sort()
    if len(changed) % 2 != 0:
        return []
    for i in range(len(changed)):
        freqDict[changed[i]] = freqDict.get(changed[i], 0) + 1
    
    if freqDict.get(0):
        if freqDict[0] % 2 == 0:
            freqDict[0] //= 2
        else:
            return []
    for k in list(freqDict):
        if k == 0:
            continue
        m = freqDict[k]
        while m > 0:
            if freqDict.get(k * 2) and freqDict[k * 2] > 0 and freqDict[k] > 0:
                freqDict[k * 2] -= 1
            elif k % 2 == 0 and freqDict.get(k // 2) and freqDict[k // 2] > 0:
                pass
            else:
                return []
            m-=1

    original = []
    for k, v in freqDict.items():
        if v!=0:
            for i in range(v):
                original.append(k)
        
            
    return original    
