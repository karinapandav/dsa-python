def reverse_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return(arr)
print(reverse_arr([1,2,3,4,5]))
print(reverse_arr([]))
print(reverse_arr([5]))
print(reverse_arr([1,1,3,3]))

