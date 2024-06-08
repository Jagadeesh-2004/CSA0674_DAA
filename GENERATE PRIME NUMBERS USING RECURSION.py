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
def generate_primes(n):
    if n <= 1:
        return []
    else:
        if is_prime(n):
            return [n] + generate_primes(n - 1)
        else:
            return generate_primes(n - 1)
n = 20
print("Prime numbers up to", n, "are:", generate_primes(n))
