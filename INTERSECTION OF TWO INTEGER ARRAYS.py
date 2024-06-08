def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 2, 4, 5, 6]
print("Intersection:", intersection(nums1, nums2))
