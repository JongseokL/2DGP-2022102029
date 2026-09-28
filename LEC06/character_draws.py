# 실습 과제 진행
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
  print('CIRCLE')
  # 캐릭터 이미지 표시
  for degree in range(360):
    theta = math.radians(degree)
    x = 400 + 200 * math.cos(theta)
    y = 300 + 200 * math.sin(theta)
    draw_character(x, y)
    pass

def draw_top():
  print('TOP')
  for x in range(50, 750, 5):
    draw_character(x, 550)
  pass

def draw_left():
  print('LEFT')
  for y in range(50, 550, 5):
    draw_character(50, y)
  pass

def draw_bottom():
  print('BOTTOM')
  for x in range(750, 50, -5):
    draw_character(x, 50)
  pass

def draw_right():
  print('BOTTOM')
  for y in range(550, 50, -5):
    draw_character(750, y)
  pass

def move_rectangle():
  print('RECTANGLE')
  draw_left()
  draw_top()
  draw_right()
  draw_bottom()
  pass

def move_line(x0, y0, x1, y1):
  n = 120
  for step in range(n+1):
    t = step / n
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t
    draw_character(x, y)


def move_CtoA():
  print('CtoA')
  move_line(400, 500, 100, 100)
  pass

def move_BtoC():
  print('BtoC')
  move_line(700, 100, 400, 500)
  pass

def move_AtoB():
  print('AtoB')
  move_line(100, 100, 700, 100)
  pass

def move_triangle():
  print('TRIANGLE')
  move_AtoB()
  move_BtoC()
  move_CtoA()
  pass


while True:
  # move_circle()
  move_rectangle()
  # move_triangle()
  pass

close_canvas()