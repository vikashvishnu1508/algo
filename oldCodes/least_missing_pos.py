def least_missing_pos(nums):
    i = 0
    n = len(nums) - 1
    flag = 1
    while i <= n:
        if nums[i] > 0:
            if flag == 1:
                min = nums[i]
                max = nums[i]
                flag = 0
            else:
                if max < nums[i]:
                    max = nums[i]
                if min > nums[i]:
                    min = nums[i]
        i += 1
    min += 1
    while min < max:
        front = 0
        end = 0
        while front < end:
            if min == nums[front] or min == nums[end]:
                break
            front += 1
            end += 1
        if front == end:
            return min
        min += 1

print(least_missing_pos([13, 18 ]))