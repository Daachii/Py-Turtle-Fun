from turtle import *

color('black', 'red')
pensize(20)

begin_fill()

pu()
goto(0, -120)
pd()

fd(30)
circle(100, 30)

pu()
goto(0, -120)
pd()

seth(-90)

fd(60)
circle(-30, 90)
fd(40)
circle(-30, 90)

fd(330)
circle(-125, 180)
fd(310)

circle(-30, 90)
fd(35)
circle(-30, 90)
fd(40)

pu()
goto(-100, -90)
pd()

seth(180)

fd(35)
circle(-30, 90)
fd(120)
circle(-50, 90)

end_fill()

pu()
goto(120, 150)
pd()

seth(180)

color('black', 'white')

begin_fill()

fd(80)
circle(50, 180)
fd(80)
circle(50, 180)

end_fill()

fillcolor('black')

done()
