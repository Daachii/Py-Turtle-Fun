from turtle import *

pensize(10)

# Tyres

pu()
goto(180, -100)
pd()

circle(90)

pu()
goto(-180, -100)
pd()

circle(90)

# Handle

pu()
goto(180, -10)
pd()

seth(140)

circle(-90, 45)
fd(100)
circle(50, 80)
fd(30)

# Frame

pu()
goto(-180, -10)
pd()

seth(-5)
fd(125)

seth(-90)
circle(25)

pu()
goto(-180, -10)
pd()

seth(55)
fd(160)

seth(0)
fd(230)

seth(-140)
fd(200)

pu()
goto(-88.23, 121.06)
pd()

seth(-70)
fd(130)

# Saddle

pu()
goto(-88.23, 121.06)
pd()

seth(110)
fd(15)

seth(0)
fd(40)
circle(5, 170)
fd(25)
circle(-10, 45)
circle(20, 90)
circle(10, 125)
fd(20)

# Pedal

pu()
goto(-31.48, -20.89)
pd()

seth(-90)
fd(45)
seth(0)
fd(10)
seth(180)
fd(20)

done()
