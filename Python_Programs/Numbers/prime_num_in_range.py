# to check for prime numbers in given range

def prime_check(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            lst.append(n)


a, b = map(int, input("Enter a b range to list prime numbers:").split())
lst = []
for n in range(a, b+1):
    prime_check(n)
print(f"List of primes in range {a} {b}: {lst}")





