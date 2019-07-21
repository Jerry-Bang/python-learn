import turtle as tl


# 画笔设置
tl.pensize(4)

# 设置初始点位置

tl.pu()
tl.goto(0, -100)
tl.pd()

# 阴鱼
tl.color('black')
tl.begin_fill()

tl.circle(100, 180)
tl.circle(50, 180)
tl.circle(-50, 180)

tl.end_fill()

# 阳鱼
tl.circle(-100, 180)

tl.pu()
tl.goto(0, -30)
tl.pd()

tl.begin_fill()
tl.circle(-20)
tl.end_fill()

tl.pu()
tl.goto(0, 30)
tl.pd()

tl.color("white")
tl.begin_fill()
tl.circle(20)
tl.end_fill()

tl.mainloop()