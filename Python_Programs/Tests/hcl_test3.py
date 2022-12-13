from itertools import groupby
import re
word = 'qwertyabcabcabcqwertyabctuvtuv'

# 1
pattern = 'abc'
print(f'{pattern} : {re.findall(pattern, word).count(pattern)}')

# 2
lst = []
for j in range(len(word)):
    for k in range(len(word)):
        if word[j:k] != '':
            lst.append(word[j:k])
new_lst = []
for a in lst:
    if lst.count(a) > 1 and len(a) > 2 and [a, lst.count(a)] not in new_lst:
        new_lst.append([a, lst.count(a)])
print(new_lst)

# 3
pattern1 = ['abc', 'tuv', 'uv']
for char in pattern1:
    count_1 = 0
    le = len(char)
    for i in range(len(word)):
        if word[i:i+le] == word[i+le:i+2*le] == char:
            count_1 += 1
    print(f'{char} {count_1}')