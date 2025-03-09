class Driver:
    def __init__(self, name, x, y):
        self.__name = name
        self.__x = x
        self.__y = y

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
        return f"{self.__name}, {self.__x}, {self.__y}"

