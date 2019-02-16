class Square:
    def __init__(self, s1):
        self.s = s1

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s, self.s, self.s, self.s)

a_square = Square(29)
print(a_square)
