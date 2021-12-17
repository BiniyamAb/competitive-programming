def isValid(s: str) -> bool:
    lst = []
    if len(s) % 2 != 0:
        return False
    for x in s:
        if x in "({[":
            lst.append(x)
        elif x in ")}]":
            if lst:
                if lst[-1] == "(":
                    if x == ")":
                        lst.pop()
                    else:
                        return False
                elif lst[-1] == "{":
                    if x == "}":
                        lst.pop()
                    else:
                        return False
                elif lst[-1] == "[":
                    if x == "]":
                        lst.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
    if lst:
        return False
    else:
        return True