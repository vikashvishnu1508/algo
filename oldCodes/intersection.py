def intersection(nums1, nums2):
    result = []
    for i in nums1:
        for j in nums2:
            if i == j:
                result.append(i)
                break
    return result

print(intersection([1, 2, 3, 4, 5], [2, 4]))

