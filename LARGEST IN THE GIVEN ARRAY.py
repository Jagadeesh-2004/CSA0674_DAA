def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [10, 324, 45, 90, 9808]
print("Largest in given array ", largest(arr))
