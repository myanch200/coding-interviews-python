def two_numbers_sum(arr,target_number):
    result = []
    for i in range(len(arr) -1):
        for j in range(len(arr) -1, 0,-1):
            if i == j:
                break
            if arr[i] + arr[j]== target_number:
                result.append(arr[j])
                result.append(arr[i])
    return result
            
            
            
    

print(two_numbers_sum([3,5,-4,8,11,1,-1,6],10))