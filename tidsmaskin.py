import pygame
import sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy

import time

from pprint import pprint as pprint

class Number():
	points = [
			numpy.array([-.5,.5]),
			numpy.array([.5,.5]),
			numpy.array([-.5,0]),
			numpy.array([.5,0]),
			numpy.array([-.5,-.5]),
			numpy.array([.5,-.5])
		]
	"""
	0 1
	2 3
	4 5
	"""

	

class Minus(Number):
	def __init__(self):
		self.order = [
			[2,3]
		]
class Zero(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[0,2],
			[1,3],
			[2,4],
			[3,5],
			[4,5],
			[1,4]
		]

class One(Number):
	def __init__(self):
		self.order = [
			[1,3],
			[3,5]
		]
class Two(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[1,3],
			[3,2],
			[2,4],
			[4,5]
		]

class Three(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[1,3],
			[3,2],
			[3,5],
			[5,4]
		]

class Four(Number):
	def __init__(self):
		self.order = [
			[0,2],
			[2,3],
			[1,3],
			[3,5]
		]

class Five(Number):
	def __init__(self):
		self.order = [
			[1,0],
			[0,2],
			[2,3],
			[3,5],
			[5,4]
		]

class Two(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[0,2],
			[3,2],
			[3,5],
			[4,5]
		]

class Six(Number):
	def __init__(self):
		self.order = [
			[0,2],
			[2,3],
			[3,5],
			[5,4],
			[4,2]
		]

class Seven(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[1,3],
			[3,5]
		]

class Eight(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[1,3],
			[2,3],
			[3,5],
			[5,4],
			[4,2],
			[2,0]
		]

class Nine(Number):
	def __init__(self):
		self.order = [
			[0,1],
			[1,3],
			[0,2],
			[2,3],
			[3,5]
		]

def render_number(number):
		glBegin(GL_LINES)
		for l in number.order:
			glVertex2f(*number.points[l[0]])
			glVertex2f(*number.points[l[1]])
		glEnd()
display = (1920,1080)
flags = pygame.DOUBLEBUF|pygame.OPENGL|pygame.FULLSCREEN|pygame.HWSURFACE
screen = pygame.display.set_mode(display, flags)

target_fps = 60



def main():
	numbers = [
		Zero(),
		One(),
		Two(),
		Three(),
		Four(),
		Five(),
		Six(),
		Seven(),
		Eight(),
		Nine(),
	]
	minus = Minus()
	startYear = [1,2,3,4,5,6,7,8,9,0]
	gotoYear = [1,8,7,6]
	framecount = 0
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(-2,0.0,-5)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == 13 or event.key == 271: # Enter or numpad-enter
					gotoYear = []
				if event.key in range(48,48+10):
					gotoYear.append(event.key-48)
				if event.key in range(256,256+10):
					gotoYear.append(event.key-256)
				print(event.key)
		glPushMatrix()
		glTranslatef(-0.1*framecount,0,0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glClearColor(0.1,0.2,0.7,1.0)
		glBegin(GL_LINES)
		glVertex2f(-1,0)
		glVertex2f(0,0)
		glVertex2f(1,framecount*0.01)
		glVertex2f(0,framecount*0.01)
		glEnd()
		glPushMatrix()
		for n in startYear:
			render_number(numbers[n])
			glTranslatef(1.1,0.0,0.0)
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(0,-1.1,0)
		for n in gotoYear:
			render_number(numbers[n])
			glTranslatef(1.1,0.0,0.0)
		glPopMatrix()
		glPopMatrix()
		pygame.display.flip()
		framecount += 0.1

if __name__ == "__main__":
	main()