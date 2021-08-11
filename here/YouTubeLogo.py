from turtle import *

pu()
goto(-250, 0)
pd()

color('#FF0000', '#FF0000')
pensize(7)

begin_fill()

for i in range(4):
	seth(88 - i * 90)
	fd(100 + (i % 2) * 100)
	circle(-50, 86)
	fd(200 - (i % 2) * 100)

end_fill()

pu()
goto(-35, 0)
pd()

color('white', 'white')
pensize(2)

begin_fill()

seth(90)
fd(65)
rt(120)
fd(130)
rt(120)
fd(130)
rt(120)
fd(65)

end_fill()

home()

done()
