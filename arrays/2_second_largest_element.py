def second_largest_element(arr):
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest 
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num 
    if second_largest == float('-inf'):
                return None
    return second_largest
print(second_largest_element([2,5,1,8,4]))        
print(second_largest_element([5,5,1,4])) 
print(second_largest_element([2]))        
print(second_largest_element([]))        
       
