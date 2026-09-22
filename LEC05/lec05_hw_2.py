from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

x = 400
y = 300
radius = 200
angle = 0.0

while True:
  x = 400 + 200 * math.cos(angle)
  y = 300 + 200 * math.sin(angle)

  clear_canvas()
  character.draw(x, y)
  update_canvas()

  angle += 0.05
  
  if angle >= 2 * math.pi:
      angle = 0

  delay(0.01)