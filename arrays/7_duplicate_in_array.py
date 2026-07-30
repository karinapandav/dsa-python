def duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)

print (duplicates([1,2,4,3,4]))   
print (duplicates([1,2,4,3]))   