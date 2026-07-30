def merged_array(arr1,arr2):
    merged_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    while i < len(arr1):
            merged_arr.append(arr1[i])
            i += 1

    return merged_arr
print(merged_array([1,5,6],[2,3,4]))