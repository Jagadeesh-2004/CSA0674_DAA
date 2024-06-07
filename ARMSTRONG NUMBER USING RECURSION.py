def is_armstrong(n, order, sum):
    if n == 0:
        return sum
    else:
        digit = n % 10
        sum += digit ** order
        return is_armstrong(n // 10, order, sum)
def check_armstrong(num):
    order = len(str(num))
    sum = is_armstrong(num, order, 0)
    if sum == num:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if check_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
