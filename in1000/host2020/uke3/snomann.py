# 03.16: Tegn en snømann

# Her kan man leke seg som man selv vil. Kan pynte i det uendelige.

from ezgraphics import GraphicsWindow

# "tegnebrett"
win = GraphicsWindow()
canvas = win.canvas()

# tittel
win.setTitle("Snowman")

# bakgrunn
canvas.setBackground("lightblue")

# bakke
canvas.setFill("lightgrey")
canvas.drawRectangle(0, 280, 400, 120)

# kropp
canvas.setFill("white")
canvas.setOutline("black")
canvas.drawOval(130, 220, 150, 150) # bunn
canvas.drawOval(154, 150, 100, 100) # midt
canvas.drawOval(170, 110, 60, 60) # hode

# hatt
canvas.setFill("black")
canvas.setOutline("black")
canvas.drawRectangle(177, 75, 50, 27) # topp
canvas.drawRectangle(167, 105, 70, 10) # bunn
canvas.setFill("red")
canvas.drawRectangle(177, 98, 50, 7) # pynt1
canvas.drawRectangle(177, 92, 50, 7) # pynt2

# nese
canvas.setFill("darkorange")
canvas.drawPolygon(204, 132, 202, 142, 245, 148) # cor1, cor2, cor3

# øyne
canvas.setFill("black")
canvas.drawOval(194, 125, 5, 5) # øye1
canvas.drawOval(211, 125, 5, 5) # øye2

win.wait()
