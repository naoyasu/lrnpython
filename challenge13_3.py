class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.hight = h

    def calculate_parameter(self):
        return 2*self.width + 2*self.hight

class Square(Shape):
    def __init__(self, w):
        self.width = w

    def calcurate_parameter(self):
        return 4*self.width

rec = Rectangle(20,30)
print(rec.calculate_parameter())

sq = Square(20)
print(sq.calcurate_parameter())

rec.what_am_i()
sq.what_am_i()
