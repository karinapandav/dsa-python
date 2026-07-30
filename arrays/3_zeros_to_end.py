def zeros_to_end(arr):
    j = 0
    for i in range(0, len(arr)):
        if arr[i] !=0:
            arr[j],arr[i] = arr[i],arr[j]
            j +=1
    return arr        
print(zeros_to_end([1,0,2,0,3,4]))
print(zeros_to_end([1,0,2,0,2,1]))
print(zeros_to_end([1,0,0]))
print(zeros_to_end([1,0]))
print(zeros_to_end([1]))
print(zeros_to_end([0]))
print(zeros_to_end([]))

