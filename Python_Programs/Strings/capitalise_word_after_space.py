def func(s):
    new = []
    for word in s.split(" "):
        new.append(word.capitalize())
    print(' '.join(new))


s = input("Enter sentence to be capitalised after space: ")
func(s)

