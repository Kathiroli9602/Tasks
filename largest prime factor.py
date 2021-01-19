def LargestPrimeFactor(n):
    primeFactor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            primeFactor = i
            n = n/i
        else:
            i = i+1

    if primeFactor < n:
        primeFactor = n

    return primeFactor

num=int(input("Enter the test number:"))
print(LargestPrimeFactor(num))

