def sub_arr(arr):
    max_sum = 0
    max_till_here = 0
    start = 0
    end = len(arr) - 1
    s = 0
    for i in range(0, len(arr)):
        max_till_here = max_till_here + arr[i]

        if max_sum < max_till_here:
            max_sum = max_till_here
            start = s
            end = i

        if max_till_here < 0:
            max_sum = 0
            s = i + 1

        print(f"Starting Index %d" % (start))
        print("Ending Index %d" % (end))
        print(f"max_sum {max_sum} max_till_here {max_till_here}")
    return max_sum


arr = [1, -3, 7, 9, 3, -4, 11, -2, 15, 8, 12, -9, 11, 4]
print(sub_arr(arr))