def sumoftwo(nums, target):
    result = []
    for i in range(1,len(nums)):
        if (  nums[i] + nums[i - 1] == target):
            result.append(i - 1)
            result.append(i)  
            break
    return result

test = [5,6,9,8,7,1,3,5,6,4]

print(sumoftwo(test, 8))