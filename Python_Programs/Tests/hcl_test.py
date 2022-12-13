word = 'rrrestarts'
# 2nd r --> $
# 2nd s --> *
lst = list(word)
count_r = 0
stop_r = 0
count_s = 0
stop_s = 0
for i in range(len(lst)):
    if lst[i] == 'r':
        count_r += 1
    if lst[i] == 's':
        count_s += 1
    if count_r == 2 and stop_r == 0:
        lst[i] = '$'
        stop_r = 1
    if count_s == 2 and stop_s == 0:
        lst[i] = '*'
        stop_s = 1
print(''.join(lst))
word1 = 'wertyrs'
print(word1.replace('r','$',2))





