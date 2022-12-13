# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = set(sorted(A))
    B = list(A)
    p_int = 0
    n_int = 0
    C = []
    for i in B:
        if i > 0:
            C.append(i)
            p_int += 1
        else:
            n_int += 1
    if n_int > 0 and p_int == 0:
        return 1
    elif p_int > 0:
        D = list(range(1, C[-1] + 1))
        for i in range(len(D)):
            if len(C) == len(D):
                return C[-1]+1
            if C[i] != D[i]:
                return D[i]

A = [1,2,3]
print(solution(A))

A = [1, 3, 5]
print(solution(A))
