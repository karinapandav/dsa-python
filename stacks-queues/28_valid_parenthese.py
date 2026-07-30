from collections import deque
def valid_parentheses(input):
    s=[]
    d = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    for ch in input:
        if ch in "[{(":
            s.append(ch)
        else:
            if not s:
                return False

            if s[-1] != d[ch]:
                return False
            else:
                s.pop()

    if not s:
        return True
    else:
        return False

print(valid_parentheses("{([)}]"))
                

        
        
