#draw rectangular

from turtle import *

class point():
	def __init__(self, x,y):
		self.x = x
		self.y = y

class rectan():
	def __init__(self, width, hight, corner):
		self.width = width
		self.hight = hight
		self.corner = corner
corner = point (10,20)
rectanqular = rectan(100,50,corner)

#def find_centre (object):
#	center = point(object.corner.x + object.width/2, object.corner.y + object.hight/2)
#	return center

#def move_rectangle():
#	dx = int(input("please enter value x to move"))
#	dy = int(input("please enter value y to move"))
#	center = find_centre(rectanqular)
#	new_x = center.x + dx
#	new_y = center.y + dy
#	new_center = point (new_x, new_y)
#	return new_center

def draw_rect():
	Screen()
	pointer = Turtle()
	pointer.shape = "circle"
	pointer.size = 2
	i = 1
	while i<=2:
		pointer.fd(rectanqular.width)
		pointer.lt(90)
		pointer.fd(rectanqular.hight)
		pointer.lt(90)
		i = i+1
	exitonclick()

print (draw_rect())
