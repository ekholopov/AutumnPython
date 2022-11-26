import turtle as t


class Plotter:
    def __init__(self, width, height):
        self.wn = t.Screen()
        self.wn.title('Plotter')
        self.wn.bgcolor("White")
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)
        self.wn.width = width
        self.wn.height = height

    def plot(self, x, y):
        min_x = x[0]
        max_x = x[0]
        for kx in x:
            if kx > max_x:
                max_x = kx
            if kx < min_x:
                min_x = kx

        min_y = y[0]
        max_y = y[0]
        for ky in y:
            if ky > max_y:
                max_y = ky
            if ky < min_y:
                min_y = ky

        tmp = t.Turtle()
        tmp.penup()
        tmp.goto(-self.wn.width/2, 0)
        tmp.pendown()

        for i in range(len(x)):
            loc_x = (x[i] - min_x)/(max_x - min_x)*self.wn.width - self.wn.width/2
            loc_y = (y[i] - min_y)/(max_y - min_y)*self.wn.height - self.wn.height/2
            tmp.goto(loc_x, loc_y)
        tmp.penup()


plotter = Plotter(400, 400)