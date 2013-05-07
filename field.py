from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Field:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	danger = 0

	def get_x(self):
		return self.x	

	def get_y(self):
		return self.y

	def get_danger(self):
		return self.danger

	def draw(self, main):
		if self.danger == 0:
			pygame.draw.rect(main.screen, main.color_field, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize))
		else:
			pygame.draw.rect(main.screen, main.color_danger, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize))
		pygame.draw.rect(main.screen, main.color_outline, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize),1)
