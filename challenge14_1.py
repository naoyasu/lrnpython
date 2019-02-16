class Square:
    square_list = []

    def __init__(self):
        self.square_list.append(self)

a = Square()
b = Square()

print(Square.square_list)
