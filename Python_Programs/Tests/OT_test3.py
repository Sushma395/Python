# print palindrome generated for N & K given
# N is length of string K is distinct letters to be used in the palindrome
# N = 10 K = 3 print oecccccceo or aoddddddoa for example
# N = 5 K = 3 print wqqw or hssh

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import string
import random


def solution(N, K):
    lst = []
    text = []
    for k in range(0, N):
        text.append('')
    for j in range(0, K):
        lst.append(random.choice(string.ascii_lowercase))
    for i in range(0, int(N/2)):
        if N % 2 == 0:
            if i == N / 2:
                text[int(N/2)] = text[int(N/2)-1] = lst[0]
                lst.remove(lst[0])
        if N % 2 != 0:
            if i == N / 2:
                text[int(N / 2)] = lst[0]
                lst.remove(lst[0])
        if text[i] == '':
            text[i] = lst[0]
            text[-(i + 1)] = lst[0]
            if len(lst) > 1:
                lst.remove(lst[0])
    print(''.join(text))


try:
    N, K = input().split()
    solution(int(N), int(K))
except EOFError as e:
    pass
