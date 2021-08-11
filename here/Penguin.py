from turtle import *

def here(x, y, fun, *args):
	pu()
	goto(x, y)
	seth(0)
	pd()

	fun(*args)

def body():
	color('#000000', '#000000')

	begin_fill()

	circle(100, 45)
	circle(200, 90)
	circle(100, 90)
	circle(200, 90)
	circle(100, 45)

	end_fill()

def belly(clr):
	color(clr, clr)

	begin_fill()

	seth(91)
	circle(130, 45)
	circle(50, 90)
	circle(130, 45)

	seth(-46)
	circle(100, 95)

	end_fill()

def nose(clr):
	color(clr, clr)

	begin_fill()

	seth(68.25)
	fd(70)

	seth(120)
	circle(30, 120)

	seth(-68.25)
	fd(70)

	end_fill()

def eye(lor):
	color('white', 'white')

	begin_fill()

	circle(40)

	end_fill()

	pu()
	seth(90)
	fd(15)
	seth(180)
	fd(lor * 5)
	pd()

	color('black', 'black')

	begin_fill()

	seth(0)
	circle(25)

	end_fill()

	pu()
	seth(90)
	fd(25)
	seth(0)
	fd(12)
	pd()

	color('white', 'white')

	begin_fill()

	circle(5, 90)
	circle(10, 90)
	circle(5, 90)
	circle(10, 90)

	end_fill()

def leg(lor, clr):
	color(clr, clr)

	begin_fill()

	fd(lor * 80)
	lt(lor * 135)
	circle(100, lor * 30)
	lt(lor * 65)
	circle(-100, lor * 25)

	end_fill()

def hand(lor):
	color('#000000', '#000000')

	seth(-90)

	begin_fill()

	lt(lor * 30)
	circle(-200 * lor, 30)
	rt(lor * 80)
	circle(-10 * lor,  80)
	fd(80)

	end_fill()

# Draw the penguin

here(0, -150, body)

here(42, -140, leg, 1, '#FF964F')

here(-42, -140, leg, -1, '#FF964F')

here(75, -103, belly, '#F5F5DC')

here(0, -40, nose, '#FF964F')

here(45, 50, eye, 1)

here(-45, 50, eye, -1)

here(130, 25, hand, 1)

here(-130, 25, hand, -1)

done()
