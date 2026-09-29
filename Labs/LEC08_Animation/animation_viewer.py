from pico2d import *

open_canvas()

background = load_image('background.png')
character = load_image('animation_sheet_hw.png')

for x in range(400, 800, 5):
    clear_canvas()
    background.draw(400, 300, 800, 600)
    character.clip_draw(0, 0, 100, 100, x, 90)
    update_canvas()
    delay (0.05)

close_canvas()