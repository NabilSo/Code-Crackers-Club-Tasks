def sumoftwo(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
test = [5,6,9,8,7,1,3,5,6,4]
print(sumoftwo(test, 8))