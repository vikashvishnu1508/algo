from math import floor

def majority_element(nums):
    map = {}
    for i in range(len(nums)):
        if nums[i] in map:
            map[nums[i]] += 1
            if map[nums[i]] > len(nums)/2:
                return nums[i]
        else:
            map[nums[i]] = 1

print(majority_element([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1]))


