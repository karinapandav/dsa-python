def anagrams(s1,s2):

    if len(s1) != len(s2):    
        return False
    
    d1 = {}
    d2 = {}

    for ch in s1:
        if ch in d1:
            d1[ch] += 1
        else:
            d1[ch] = 1

    for ch in s2:
        if ch in d2:
            d2[ch] += 1
        else:
            d2[ch] = 1
        
    return d1 == d2
print(anagrams("anagram","nagaram"))
print(anagrams("hoia","ohla"))
print(anagrams("holla","ohla"))



def anagrams(s1,s2):

    if len(s1) != len(s2):    
        return False
    
    d = {}

    for ch in s1:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    for ch in s2:
        if ch not in d:
            return False
        else:
            d[ch] -= 1

    for count in d.values():
        if count != 0:
            return False
       
    return True    
print(anagrams("anagram","nagaram"))
print(anagrams("hoia","ohla"))
print(anagrams("holla","ohla"))
