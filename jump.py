from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from field import *

class Starter(PygameHelper):
	def __init__(self):
		self.w, self.h = 800, 600
		PygameHelper.__init__(self, size=(self.w, self.h), fill=((0,0,0)))

	fieldsize = 100
	fields = []
	for i in range(5):
		for j in range(5):
			f = Field(i, j)
			fields.append(f)
	color_field = (255,255,255)
	color_outline = (255,0,0)
	color_player = (0,255,0)
	color_danger = (0,0,255)
	player = (0,0)

	def update(self):
		pass

	def keyDown(self, key):
		pass

	def keyUp(self, key):
		pass

	def mouseDown(self, button, pos):
		print('button down at: ', pos)
		for field in self.fields:
			print('testing field at: ', field.get_x(), field.get_y())
			if pos[0] > field.get_x()*self.fieldsize and pos[0] < field.get_x()*self.fieldsize+self.fieldsize and pos[1] > field.get_y()*self.fieldsize and pos[1] < field.get_y()*self.fieldsize+self.fieldsize:
				self.player = (field.get_x(), field.get_y())
		print('player at: ', self.player)


	def mouseUp(self, button, pos):
		pass

	def mouseMotion(self, buttons, pos, rel):
		pass

	def draw(self):
		for field in self.fields:
			field.draw(self)
		pygame.draw.rect(self.screen, self.color_player, (self.player[0]*self.fieldsize, self.player[1]*self.fieldsize, self.fieldsize, self.fieldsize))

s = Starter()
s.mainLoop(40)
