class CountStr:

    def __init__(self, s):
        self.s = s

    def cnt(self):
        for char in self.s:
            if char != ' ':
                print(f'{char}:{s.count(char)}')


s = 'This is test program'
c = CountStr(s)
c.cnt()






