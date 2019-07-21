import turtle as tl

from datetime import *


# api
def goto(hdl, dis):
    hdl.pu()
    hdl.fd(dis)
    hdl.pd()


def indicator(name, length):
    goto(tl, -length * 0.1)
    tl.begin_poly()
    tl.fd(length * 1.1)
    tl.end_poly()
    sh = tl.get_poly()
    tl.register_shape(name, sh)
    tl.reset()


# 基础设置
tl.mode('logo')
tl.hideturtle()
tl.tracer(False)

# 创建表盘
clock_dial = tl.Turtle()
clock_dial.hideturtle()

for tick in range(60):
    goto(clock_dial, 100)
    if tick % 5 == 0:
        clock_dial.fd(20)
        if tick == 0:
            clock = 12
        else:
            clock = tick / 5
        clock_dial.write(int(clock))
        goto(clock_dial, -120)
    else:
        clock_dial.dot(5)
        goto(clock_dial, -100)

    clock_dial.right(6)

# 创建指针
second = tl.Turtle()
minute = tl.Turtle()
hour = tl.Turtle()

indicator("second", 100)
indicator("minute", 80)
indicator("hour", 50)

second.shape("second")
minute.shape("minute")
hour.shape("hour")

second.shapesize(1, 1, 4)
minute.shapesize(1, 1, 4)
hour.shapesize(1, 1, 4)

tl.tracer(True)


def showtime():
    dt = datetime.today()
    s = dt.second + dt.microsecond * 0.000001
    m = dt.minute + s / 60.0
    h = dt.hour + m / 60.0

    second.setheading(6 * s)
    minute.setheading(6 * m)
    hour.setheading(30 * h)

    tl.ontimer(showtime, 100)


showtime()

tl.mainloop()
