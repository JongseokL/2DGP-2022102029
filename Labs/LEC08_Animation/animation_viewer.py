from pico2d import *

open_canvas()

background = load_image('background.png')
character = load_image('animation_sheet_hw.png')

for x in range(800, 0, -5):
    clear_canvas()
    background.draw(400, 300, 800, 600)
    update_canvas()
    delay (0.05)

close_canvas()