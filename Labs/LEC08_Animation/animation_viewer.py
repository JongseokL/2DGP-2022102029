from pico2d import *

open_canvas()

background = load_image('background.png')
character = load_image('animation_sheet_hw.png')

for x in range(100, 700, 5):
    clear_canvas()
    background.draw(400, 300, 800, 600)
    character.clip_draw(45, 785, 120, 210, x, 300, 85, 150)
    update_canvas()
    delay (0.05)

close_canvas()