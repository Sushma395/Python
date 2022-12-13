def strip_punc(s):
    invalid_p = '''!"#$%&'()*+/:;<=>@[\]^_`{|}~'''
    valid_p = '''.,?'''
    s1 = s.translate(str.maketrans("", "", valid_p))
    lst = s1.split()
    print(lst)
    i = 0
    while i < len(lst):
        for char in lst[i]:
            if char in invalid_p or char.isdigit():
                lst.pop(i)
                i = i - 1
                break
        i = i + 1
        print(lst)
        print(f'i : {i} , len : {len(lst)}')
    return len(lst)


s = '''he is a good programmer , he won 865 competitions#, but sometimes he dont. 
    What do you think? All test-cases should pass. Done-done?'''

print(strip_punc(s))
