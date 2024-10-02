# CUSTOM CLASSES IN PYTHON 


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    #  the __iter__ method  is used to make the class iterable
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rectangle = Rectangle(10, 5)


for dimension in rectangle:
    print(dimension)
