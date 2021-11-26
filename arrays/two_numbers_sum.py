def two_numbers_sum(arr,target_number):
    result = {}
    for i in arr:
        if target_number - i in result:
            return [target_number- i,i]
        else:
            result[i] = True
    return []
            
    
            
            
            
    

print(two_numbers_sum([3,5,-4,8,11,1,-1,6],10))