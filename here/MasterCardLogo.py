from turtle import *

pensize(7)

pu()
goto(-99, -150)
pd()

color('#EB001B', '#EB001B')
begin_fill()
circle(150)
end_fill()

pu()
goto(99, -150)
pd()

color('#F79E1B', '#F79E1B')
begin_fill()
circle(150)
end_fill()

pu()
goto(0, 112.69)
pd()

color('#FF5F00', '#FF5F00')
begin_fill()
seth(-139)
circle(150, 99)
seth(41)
circle(150, 99)
end_fill()

done()
