from pico2d import *

open_canvas()

background = load_image('background.png')
character = load_image('animation_sheet_hw.png')

frames = [
    (45,  785, 120, 210),
    (225, 785, 150, 210),
    (415, 782, 145, 215),
    (600, 782, 155, 215),
    (785, 782, 165, 215),
    (995, 785, 135, 210)
]

frame = 0

for x in range(100, 700, 5):
    clear_canvas()
    background.draw(400, 300, 800, 600)
    sx, sy, sw, sh = frames[frame]
    character.clip_draw(sx, sy, sw, sh, x, 300, 85, 150)
    update_canvas()
    frame = (frame + 1) % 6
    delay (0.05)

close_canvas()