from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

x = 50
y = 50

while (True):
  if (x < 750 and y == 50):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    x += 2
    delay(0.01)

  elif (x >= 750 and y < 550):
   clear_canvas()
   character.draw(x, y)
   update_canvas()
   y += 2
   delay(0.01)

  elif (x > 50 and y >= 550):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    x -= 2
    delay(0.01)

  elif (x <= 50 and y > 50):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    y -= 2
    delay(0.01)