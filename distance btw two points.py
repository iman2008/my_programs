#calculating distance between two points

import math

class point ():
	def __init__(self, x,y):
		self.x = x
		self.y = y


def distance(k1,k2):
	temp = math.sqrt((k2.y - k1.y)**2 + (k2.x - k1.x)**2)
	return temp

p1 = point (10,20)
p2 = point (5,10)

print (distance (p1,p2))
