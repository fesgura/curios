import math
import turtle

# draw the circle using turtle
def drawCircle(x, y, r):
    # move to the start of circle
    turtle.up() # "lifts the pen" so it won't draw
    turtle.setpos(x + r, y) # positions the pen
    turtle.down() # "lowers the pen" so it can start drawing
    # draw the circle
    for i in range(0, 365, 5): # [0,365) in steps of 5 (0, 4, 9, ..., 364)
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a)) # draws circle using the parametric equations x = r * cos(a) and y = r * sen(a)
        
        
drawCircle(100, 100, 50) # draws circle of radius 50 with center in 100, 100
turtle.mainloop()