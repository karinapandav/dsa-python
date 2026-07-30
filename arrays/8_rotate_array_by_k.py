#brute force code
def rotate(arr,k):
    for j in range(k):
        last = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            arr[i+1] = arr [i]
        arr[0]=last
    return arr
print(rotate([1,2,3,4,5,6,7],3))

#optimal code
def reverse(left, right, arr):
    while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    return arr 

def rotate(arr,k):
    k = k % len(arr)
    reverse(0 ,len(arr)-1, arr)
    reverse (0, k-1, arr)
    reverse(k,len(arr)-1, arr)
    return arr
print(rotate([1,2,3,4,5,6,7],3))