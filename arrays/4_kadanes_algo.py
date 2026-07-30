def kadanes(arr):
    if not arr:
        return None
    
    current_sum = 0
    max_sum= arr[0]
    
    for num in arr:
        current_sum += num
        max_sum = max(current_sum, max_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum
print(kadanes([2,3,1]))        
print(kadanes([-2,-3,-1]))              
print(kadanes([]))        
print(kadanes([3,-1]))        
print(kadanes([3]))        
print(kadanes([10,3,-1]))        
print(kadanes([-2,3,10]))        
