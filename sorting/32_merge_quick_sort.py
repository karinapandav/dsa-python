def merge(left, right):
    lt = 0
    rt = 0
    ans = []

    while lt < len(left) and rt < len(right):

        if left[lt] <= right[rt]:
            ans.append(left[lt])
            lt += 1
        else:
            ans.append(right[rt])
            rt += 1

    while lt < len(left):
        ans.append(left[lt])
        lt += 1

    while rt < len(right):
        ans.append(right[rt])
        rt += 1

    return ans


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right) 
print(merge_sort([1,3,5,2,8,9]))    

def partition(arr, low, high):
    pivot =  arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        

    arr[i+1], arr[high] = arr[high] , arr[i+1]
    return i + 1 
            

def quick_sort(arr, low, high):
    if low < high:
        return arr

    p = partition(arr,low,high)
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1 , high)

    arr = quick_sort(arr, 0, len(arr)-1)
    print(arr)
      
