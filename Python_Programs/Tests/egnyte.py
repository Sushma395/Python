index = [1, 2, 3]
languages = ['python', 'c', 'c++']

e = {}
e[1] = languages[0]
print(e)
d = {}
for i in index:
    for j in range(len(languages)):
        d[i] = languages[j]

print(d)

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
common = []

[common.append(i) for i in s1 for j in s2 if i == j]

for i in s1:
    for j in s2:
        if i == j:
            common.append(i)

print(common)

vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'

for vowel in vowels:
    print(f'{vowel}: {ip_str.count(vowel)}')
