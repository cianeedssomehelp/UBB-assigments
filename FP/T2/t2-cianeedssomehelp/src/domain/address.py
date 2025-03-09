class Address:
    def __init__(self, add_id, name, x, y):
        self.__address_id = add_id
        self.__name = name
        self.__x = x
        self.__y = y

    @property
    def address_id(self):
        return self.__address_id
    @property
    def name(self):
        return self.__name
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    def __str__(self):
        return f"{self.address_id}, {self.name}, {self.x}, {self.y}"
    def __eq__(self, other):
        return self.__address_id == other.address_id
