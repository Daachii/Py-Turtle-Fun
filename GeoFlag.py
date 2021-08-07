from turtle import *

f = Turtle()

f.pu()
f.setpos(-370, 240)
f.pd()

f.fd(740)
f.rt(90)
f.fd(480)
f.rt(90)
f.fd(740)
f.rt(90)
f.fd(480)

f.color('red', 'red')

f.seth(0)
f.pu()
f.setpos(-50, 50)
f.pd()

mainag = [90, -90, -90, 90, -90, -90, 90, -90, -90, 90, -90, -90]
mainfd = [190, 100, 190, 320, 100, 320, 190, 100, 190, 320, 100, 320]

f.begin_fill()

for i in range(len(mainfd)):
	f.lt(mainag[i])
	f.fd(mainfd[i])

f.end_fill()

f.seth(0)
f.pu()
f.setpos(-225, 160)
f.pd()

smallag = [100, -100, -100, 110, -100, -100, 110, -100, -100, 110, -100, -100]
smallfd = [35, 30, 35, 35, 30, 35, 35, 30, 35, 35, 30, 35]

f.begin_fill()

for i in range(len(smallfd)):
	f.lt(smallag[i])
	f.fd(smallfd[i])

f.end_fill()

f.seth(0)
f.pu()
f.setpos(200, 160)
f.pd()

f.begin_fill()

for i in range(len(smallfd)):
	f.lt(smallag[i])
	f.fd(smallfd[i])

f.end_fill()

f.seth(0)
f.pu()
f.setpos(195, -145)
f.pd()

f.begin_fill()

for i in range(len(smallfd)):
	f.lt(smallag[i])
	f.fd(smallfd[i])

f.end_fill()

f.seth(0)
f.pu()
f.setpos(-225, -145)
f.pd()

f.begin_fill()

for i in range(len(smallfd)):
	f.lt(smallag[i])
	f.fd(smallfd[i])

f.end_fill()

f.pu()
f.setpos(0, 0)
f.pd()

done()
