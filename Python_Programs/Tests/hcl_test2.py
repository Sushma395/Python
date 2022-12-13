#("Python") -> "16 25 20 8 15 14"
word = 'Python exam'
#approach 1
lst = []
print(word.split())
for i in word:
    print(ord(i.lower()) - 96,end=" ")
print('\n')
#approach 2
lst1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in word:
    if i in lst1:
        print(int(lst1.index(i.lower()))+1,end=" ")
print('\n')
import string
lst2 = list(string.ascii_lowercase)
for i in word:
    if i in lst2:
        print(int(lst1.index(i.lower()))+1,end=" ")
