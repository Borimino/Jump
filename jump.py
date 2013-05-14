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
		f = open(self.lvlname)
		lines = f.readlines()
		for line in lines:
			coords = line.split()
			f2 = Field(x=int(coords[0]), y=int(coords[1]))
			if int(coords[2]) == 2:
				f2.danger = 2
			#f2.danger = int(coords[2])
			if int(coords[2]) == 1:
				self.player = (int(coords[0]), int(coords[1]))
			if int(coords[2]) == 3:
				f2.goal = True
			self.fields.append(f2)
		for field in self.fields:
			field.is_danger(self)
		for field in self.fields:
			#print("x = ", field.x, " & y = ", field.y, " & d = ", field.danger)
			pass

	lvlnr = 1
	lvlname = "lvl" + str(lvlnr) + ".txt" 
	fieldsize = 100
	fields = []
	color_field = (255,255,255)
	color_outline = (255,0,0)
	color_player = (255,0,0)
	color_danger = (0,0,255)
	color_available = (0,255,0)
	color_bg = (0,0,0)
	player = (0,0)
	path = (1,2)

	def reload(self):
		self.fields = []
		f = open(self.lvlname)
		print(self.lvlname)
		lines = f.readlines()
		for line in lines:
			coords = line.split()
			f2 = Field(x=int(coords[0]), y=int(coords[1]))
			if int(coords[2]) == 2:
				f2.danger = 2
			#f2.danger = int(coords[2])
			if int(coords[2]) == 1:
				self.player = (int(coords[0]), int(coords[1]))
			if int(coords[2]) == 3:
				f2.goal = True
			self.fields.append(f2)
		for field in self.fields:
			field.is_danger(self)
		for field in self.fields:
			#print("x = ", field.x, " & y = ", field.y, " & d = ", field.danger)
			pass

	def update(self):
		pass

	def keyDown(self, key):
		pass

	def keyUp(self, key):
		pass

	def mouseDown(self, button, pos):
		for field in self.fields:
			if pos[0] > field.get_x()*self.fieldsize and pos[0] < field.get_x()*self.fieldsize+self.fieldsize and pos[1] > field.get_y()*self.fieldsize and pos[1] < field.get_y()*self.fieldsize+self.fieldsize:
				if field.is_available(self) == 1:
					self.player = (field.get_x(), field.get_y())
					if field.goal == True:
						self.lvlnr += 1
						self.lvlname = "lvl" + str(self.lvlnr) + ".txt"
						self.reload()


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
