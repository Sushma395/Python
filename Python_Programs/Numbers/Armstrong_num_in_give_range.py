# if the number obtained totals to or equals the original number
# when each of the digits is raised to the power of the number of digits in the number and added to obtain a number,
# in any given number system, such a number is called an Armstrong number.

a, b = map(int, input("Enter a b to check Armstrong in that range: ").split(" "))
print(a, b)
lst = []
for num in range(a, b+1):
    new_num = num
    length = len(str(num))
    add = 0
    while new_num != 0:
        add += (new_num % 10) ** length
        new_num = new_num // 10  #floor division
    if add == num:
        lst.append(num)
print(f"List of Armstrong's in range of {a} {b}: {lst}")