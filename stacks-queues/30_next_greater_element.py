def next_greater_element(arr):
    s = []
    ans = []
    for i in range(len(arr)-1, -1, -1):
        current = arr[i]
        while s and s[-1] <= current:
            s.pop()

        if not s:
                ans.append(-1)
        else:
                ans.append(s[-1])

        s.append(current)

    ans.reverse()
    return ans
print(next_greater_element([2,1,3]))
                        