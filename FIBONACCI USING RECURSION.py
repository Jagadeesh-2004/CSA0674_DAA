def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
nterms = int(input("Enter the number of terms: "))
print("Fibonacci sequence: ")
for i in range(nterms):
    print(fibonacci(i))
