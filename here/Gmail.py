from turtle import *

def start_point(ang, crd):
	seth(ang)
	pu()
	goto(crd)
	pd()

def cinnabar_part():
	color('#EA4335', '#EA4335')

	begin_fill()

	lt(38)
	fd(285)
	
	global sy_sg_st
	sy_sg_st = pos()

	lt(52)
	fd(245)

	lt(128)
	fd(285)

	rt(76)
	fd(285)

	lt(128)
	fd(245)

	global hc_bb_st
	hc_bb_st = pos()

	lt(52)
	fd(285)

	end_fill()

def sy_hc_part(i, clr):
	color(clr, clr)

	begin_fill()

	lt(i * 38)
	fd(245)

	lt(i * 52)
	fd(101)

	circle(i * 70, 128)
	fd(101)

	lt(i * 52)
	fd(245)

	end_fill()

def sg_bb_part(i, clr):
	color(clr, clr)

	begin_fill()
	
	lt(i * 38)
	fd(245)

	rt(i * 128)
	fd(450)

	circle(i * (-50), 90)
	fd(143)

	rt(i * 90)
	fd(349)

	end_fill()

start_point(0, (0, -150))
cinnabar_part()

start_point(0, sy_sg_st)
sy_hc_part(1, '#FBBC05')

start_point(0, sy_sg_st)
sg_bb_part(1, '#34A853')

start_point(180, hc_bb_st)
sy_hc_part(-1, '#BB001B')

start_point(180, hc_bb_st)
sg_bb_part(-1, '#4285F4')

hideturtle()

done()
