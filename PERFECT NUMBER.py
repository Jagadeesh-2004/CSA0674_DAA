def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
num = 6
print(num, "is a perfect number" if is_perfect(num) else "is not a perfect number")
