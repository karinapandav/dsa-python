def prefix(strs):
    shortest = min(strs, key=len)

    prefix = ""

    for i in range(len(shortest)):
        for word in strs:
            if word[i] != shortest[i]:
                return prefix
            
        prefix += shortest[i]
    return prefix            
            

print(prefix(["flower","flow","fly","flight"]))
print(prefix(["lower","flow","fly","flight"]))
print(prefix(["dogs","dog","fly","flight"]))
