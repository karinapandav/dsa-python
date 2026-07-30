def two_sum(nums,target):
    d = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in d:
            return d[needed], i
        else:
            d[num] = i
print(two_sum([2,7,11,15],9))        
print(two_sum([2,7,1],8))            
print(two_sum([2,7,7,15],7))            
print(two_sum([2,3,1,2],3)) 
print(two_sum([2,5],3)) 
print(two_sum([2],3)) 
print(two_sum([],3)) 
           
