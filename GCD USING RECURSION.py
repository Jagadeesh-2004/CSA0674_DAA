def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)
a = 60
b = 48
print("The gcd of 60 and 48 is : ", gcd(a, b))
