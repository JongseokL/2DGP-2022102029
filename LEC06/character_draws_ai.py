from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
	clear_canvas()
	character.draw(x, y)
	update_canvas()
	delay(0.01)


def move_circle():
	radius = 200
	center_x, center_y = 400, 300
	for degree in range(360):
		angle = math.radians(degree)
		x = center_x + radius * math.cos(angle)
		y = center_y + radius * math.sin(angle)
		draw_character(x, y)


move_circle()
close_canvas()
