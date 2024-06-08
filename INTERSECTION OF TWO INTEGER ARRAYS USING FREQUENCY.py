def intersection_with_frequency(nums1, nums2):
    freq1 = {}
    freq2 = {}
    for num in nums1:
        freq1[num] = freq1.get(num, 0) + 1
    for num in nums2:
        freq2[num] = freq2.get(num, 0) + 1
    intersection = []
    for num in freq1:
        if num in freq2:
            intersection.extend([num] * min(freq1[num], freq2[num]))
    return intersection
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 2, 4, 5, 6]
print("Intersection with frequency:", intersection_with_frequency(nums1, nums2))
