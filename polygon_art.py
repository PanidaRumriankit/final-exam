"""Draw polygons"""
import turtle
import random


class Polygon:
    """Class use for draw polygons"""
    def __init__(self):
        """initialize variable in class"""
        gen = int(input("Which art do you want to generate? "
                        "Enter a number between 1 to 8, inclusive: "))
        self.__gen = gen
        self.__size = self.get_new_size()
        self.__orientation = self.get_new_orientation()
        self.__location = self.get_new_location()
        self.__color = self.get_new_color()
        self.__border_size = self.get_new_border_size()
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def draw_polygon(self):
        '''draw 30 polygons'''
        for _ in range(30):
            turtle.penup()
            self.draw()
            turtle.pendown()
            inside = 0
            side = 0
            if self.__gen < 4:
                side = self.__gen + 2
            elif self.__gen == 4:
                side = random.randint(3, 5)
            elif self.__gen < 8:
                side = self.__gen - 2
                inside = 1
            elif self.__gen == 8:
                side = random.randint(3, 5)
                inside = 1
            for _ in range(side):
                turtle.forward(self.__size)
                turtle.left(360 / side)
            turtle.penup()
            if inside:
                self.get_inside(side, 1)
            self.draw()
            self.__size = self.get_new_size()
            self.__orientation = self.get_new_orientation()
            self.__location = self.get_new_location()
            self.__color = self.get_new_color()
            self.__border_size = self.get_new_border_size()

    def draw(self):
        """use to prepare to draw"""
        turtle.goto(self.__location[0], self.__location[1])
        turtle.setheading(self.__orientation)
        turtle.color(self.__color)
        turtle.pensize(self.__border_size)

    def get_new_color(self):
        """use to get a new color for a polygon"""
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def get_new_location(self):
        """use to get a new location for a polygon"""
        return [random.randint(-300, 300), random.randint(-200, 200)]

    def get_new_size(self):
        """use to get a new self.__size for polygon"""
        return random.randint(50, 150)

    def get_new_orientation(self):
        """use to get a new orientation for polygon"""
        return random.randint(0, 90)

    def get_new_border_size(self):
        """use to get a new border size for polygon"""
        return random.randint(1, 10)

    def get_inside(self, side, num):
        """use to get an in side art for polygon"""
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.__size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.__size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.__location[0] = turtle.pos()[0]
        self.__location[1] = turtle.pos()[1]
        self.__size *= reduction_ratio
        turtle.penup()
        self.draw()
        turtle.pendown()
        for _ in range(side):
            turtle.forward(self.__size)
            turtle.left(360 / side)
        turtle.penup()
        if num:
            num -= 1
            self.get_inside(side, num)


p = Polygon()
p.draw_polygon()
turtle.done()
