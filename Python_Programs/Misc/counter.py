from collections import Counter

# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# with dictionary
count = Counter({'A': 3, 'B': 5, 'C': 2})
print(count)

count.update(['A', 1])
print(count)

s = Counter('Need to count occurrence of alphabets in given string')
print(s)
print("Most common:")
print(s.most_common())
s.update(['$',2])
print(s)
s.popitem()
s.popitem()
print(s)
