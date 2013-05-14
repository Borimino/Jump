from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Field:
	def __init__(self, pos=(-1,-1), x=0, y=0):
		self.x = x
		self.y = y
		if pos[0] != -1 and pos[1] != -1:
			self.x = pos[0]
			self.y = pos[1]

	danger = 0
	available = 0
	goal = False

	def get_x(self):
		return self.x	

	def get_y(self):
		return self.y

	def get_danger(self):
		return self.danger

	def is_danger(self, main):
		if self.danger == 2:
			return
		for field in main.fields:
			if field.x == self.x and field.y == self.y:
				continue	
			if (field.x - self.x) == (field.y - self.y):
				if field.danger == 2:
					self.danger = 1
					return
			if (self.x - field.x) == (field.y - self.y):
				if field.danger == 2:
					self.danger = 1
					return
			if (field.x - self.x) == (self.y - field.y):
				if field.danger == 2:
					self.danger = 1
					return
			if (self.x - field.x) == (self.y - field.y):
				if field.danger == 2:
					self.danger = 1
					return
		self.danger = 0

	def draw(self, main):
		if self.danger == 0:
			pygame.draw.rect(main.screen, main.color_field, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize))
			if self.is_available(main) == 1:
				pygame.draw.rect(main.screen, main.color_available, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize))
				pygame.draw.rect(main.screen, main.color_outline, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize),1)
		elif self.danger == 1:
			pygame.draw.rect(main.screen, main.color_danger, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize))
			pygame.draw.rect(main.screen, main.color_outline, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize),1)
		elif self.danger == 2:
			pygame.draw.rect(main.screen, main.color_bg, (self.x*main.fieldsize, self.y*main.fieldsize, main.fieldsize, main.fieldsize))
		else:
			pass
	
	def is_available(self, main):
		if self.danger == 1:
			return 0
		if main.player[0] + main.path[0] == self.x and main.player[1] + main.path[1] == self.y:
			return 1
		if main.player[0] - main.path[0] == self.x and main.player[1] + main.path[1] == self.y:
			return 1
		if main.player[0] + main.path[0] == self.x and main.player[1] - main.path[1] == self.y:
			return 1
		if main.player[0] - main.path[0] == self.x and main.player[1] - main.path[1] == self.y:
			return 1
		if main.player[0] + main.path[1] == self.x and main.player[1] + main.path[0] == self.y:
			return 1
		if main.player[0] - main.path[1] == self.x and main.player[1] + main.path[0] == self.y:
			return 1
		if main.player[0] + main.path[1] == self.x and main.player[1] - main.path[0] == self.y:
			return 1
		if main.player[0] - main.path[1] == self.x and main.player[1] - main.path[0] == self.y:
			return 1
