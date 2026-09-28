# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def draw_top():
  print('TOP')
  pass

def draw_left():
  print('LEFT')
  pass

def draw_bottom():
  print('BOTTOM')
  pass

def draw_right():
  print('BOTTOM')
  pass


def move_circle():
  print('CIRCLE')
  # 캐릭터 이미지 표시
  for degree in range(360):
    theta = math.radians(degree)
    x = 400 + 200 * math.cos(theta)
    y = 300 + 200 * math.sin(theta)
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    pass

def move_rectangle():
  print('RECTANGLE')
  draw_top()
  draw_left()
  draw_bottom()
  draw_right()
  pass

def move_triangle():
  print('TRIANGLE')
  pass


while True:
  move_circle()
  move_rectangle()
  move_triangle()

close_canvas()