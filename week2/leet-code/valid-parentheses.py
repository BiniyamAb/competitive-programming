def isValid(s: str) -> bool:
    lst = []
    if len(s) % 2 != 0: return False
    tags = {"{": "}", "[": "]", "(": ")"}
    for x in s:
        if x in "({[":
            lst.append(x)
        elif x in ")}]":
            if lst:
                if x == tags[lst[-1]]:
                    lst.pop()
                else:
                    return False
            else:
                return False
            
    return False if lst else True