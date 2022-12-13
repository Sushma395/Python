# to print fibonacci series till nth number

def fibo(num):
    a = 0
    b = 1
    if num == 1:
        print(a, end=" ")
    elif num >= 2:
        print(a, b, end=" ")
        count = 3
        while count <= num:
            a, b = b, a+b
            print(b, end=" ")
            count += 1
    else:
        print("Enter correct number")


num = int(input("Enter num to print till Nth Fibonacci number:"))
fibo(num)
