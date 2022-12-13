def myfunc(s):
    j = []
    s = list(s)
    for i in s:
        if s.index(i)%2 != 0:
            i = i.lower()
            j.append(i)
        else:
            i = i.upper()
            j.append(i)
    return ''.join(j)

t = myfunc('Missippi')
print(t)