def subarray_with_sum_zero(arr):
    prefix_sum = 0
    seen = set()
    for i in arr:
        prefix_sum += i
        if prefix_sum == 0:
            return True
        elif prefix_sum in seen:
            return True
        else:
            seen.add(prefix_sum)
    return False
print(subarray_with_sum_zero([4,2,-3,1,6]))        
print(subarray_with_sum_zero([4,2,3,1,6]))        
print(subarray_with_sum_zero([0,2,-3,1,6]))        
print(subarray_with_sum_zero([4,-2,3,-1,6,6])) 