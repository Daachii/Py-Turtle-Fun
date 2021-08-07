from turtle import *

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

bgcolor('black')

speed(10)

for i in range(360):
	pencolor(colors[i % 6])
	width(i / 100 + 1)
	fd(i)
	lt(59)

done()
