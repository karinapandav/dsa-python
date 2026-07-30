def remove_duplicates(s):
    seen = set()
    ans = ""
    for ch in s:
        if ch not in seen:
            ans += ch
            seen.add(ch)
           
    return ans 
print(remove_duplicates("karina"))        