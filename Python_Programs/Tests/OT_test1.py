# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.8.10
    lst = list(S)
    for i in range(0, len(lst)+1):
        print(i)
        if i == 0:
            if lst[i] != 'a' and lst[i+1] != 'a':
                lst.insert(0, 'aa')
        if i == len(lst)+1:
            #if lst[i] != 'a' and lst[i-1] != 'a':
            lst.append('aa')
        if lst[i] == 'aa' or (lst[i] == 'a' and lst[i+1] == 'a'):
            pass
        else:
            lst.insert(i+1, 'aa')
        print(lst)

try:
    S = input('string: ')
    solution(S)
except EOFError as e:
    pass