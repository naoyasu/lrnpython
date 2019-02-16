# http://tinyurl.com/gt28gww

class Person:
    def __init__(self):
        self.name = "Nob"

nob = Person()
same_nob = nob
print(nob is same_nob)

another_nob = Person()
print(nob is another_nob)
