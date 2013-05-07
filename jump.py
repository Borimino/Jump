from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Starter(PygameHelper):
	def __init__(self):
		self.w, self.h = 800, 600
		PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

	fieldsize = 100
	fields = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]

	def update(self):
		pass

	def keyDown(self, key):
		pass

	def keyUp(self, key):
		pass

	def mouseDown(self, button, pos):
		pass

	def mouseUp(self, button, pos):
		pass

	def mouseMotion(self, buttons, pos, rel):
		pass

	def draw(self):
		for field in self.fields:
			pygame.draw.rect(self.screen, (0,0,0), (field[0]*self.fieldsize, field[1]*self.fieldsize, self.fieldsize, self.fieldsize))

s = Starter()
s.mainLoop(40)
