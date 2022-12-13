# to print list of fibonacci series till nth number

def fibo(num):
    a = 0
    b = 1
    lst = []
    if num == 1:
        return lst.append(a)
    elif num >= 2:
        lst.extend([a, b])
        while len(lst) < num:
            a, b = b, a+b
            lst.append(b)
        return lst
    else:
        print("Enter correct number")


num = int(input("Enter num to list till Nth Fibonacci number:"))
output = fibo(num)
print(output)