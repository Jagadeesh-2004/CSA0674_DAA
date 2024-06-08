def reverse_num(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return reverse_num(n // 10, rev)
num = 12345
print("Reverse of", num, "is", reverse_num(num))
