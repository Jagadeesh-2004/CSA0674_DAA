def is_prime(n, i=2):
    if n <= 2:
        if n == 2:
            return True
        else:
            return False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)
num = 17
print(num, "is prime" if is_prime(num) else "is not prime")
