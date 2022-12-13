# if list is [130, 191, 200, 10, 101] , print max sum of 2 numbers in list, having same first and last digits
# if nothing matches the given condition return -1
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    lst = []
    for i in A:
        lst.extend([list(map(int, str(i)))])
    new_lst = []
    for j in range(0, len(lst)):
        for k in range(0, len(lst)):
            if lst[j][0] == lst[k][0] and lst[j][-1] == lst[k][-1] and j != k :
                if A[j]+A[k] not in new_lst:
                    new_lst.append(A[j]+A[k])
    if len(new_lst) == 0:
        return -1
    else:
        # return new_lst
        return max(new_lst)



try:
    A = [130, 191, 200, 10, 101, 101]
    print(solution(A))
except EOFError as e:
    pass
