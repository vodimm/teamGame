from turtle import *


'''

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


'''
color('red', 'yellow')

color_r,color_g,color_b=0,0,0
while True:
    
    color(255,0,0)
    forward(2)
    left(1)
done()#pause


while True:

    color(color_r,color_g,color_b)
    forward(2)
    left(1)
    color_r+=1



done()#pause