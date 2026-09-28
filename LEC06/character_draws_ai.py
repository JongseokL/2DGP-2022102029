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


def move_rectangle():
	for x in range(50, 751, 5):
		draw_character(x, 550)
	for y in range(550, 49, -5):
		draw_character(750, y)
	for x in range(750, 49, -5):
		draw_character(x, 50)
	for y in range(50, 551, 5):
		draw_character(50, y)


def move_line(start, end):
	start_x, start_y = start
	end_x, end_y = end
	distance = math.hypot(end_x - start_x, end_y - start_y)
	steps = max(1, int(distance / 5))

	for step in range(steps + 1):
		t = step / steps
		x = start_x + (end_x - start_x) * t
		y = start_y + (end_y - start_y) * t
		draw_character(x, y)


def move_triangle():
	point_a = (100, 100)
	point_b = (700, 100)
	point_c = (400, 500)
	move_line(point_a, point_b)
	move_line(point_b, point_c)
	move_line(point_c, point_a)


move_circle()
move_rectangle()
move_triangle()
close_canvas()
