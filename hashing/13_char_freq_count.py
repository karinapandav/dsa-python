def char_freq_count(s):
   
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d
print(char_freq_count("banana"))        
