class Rectangle():
    def __init__(self, w, h):
        self.width = w
        self.hight = h

    def calculate_parameter(self):
        return 2*self.width + 2*self.hight

class Square():
    def __init__(self, w):
        self.width = w

    def calcurate_parameter(self):
        return 4*self.width

    def change_size(self, n):
        self.width += n
        

rec = Rectangle(20,30)
print(rec.calculate_parameter())

sq = Square(20)
print(sq.calcurate_parameter())

sq.change_size(200)
print(sq.width)
