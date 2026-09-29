from pico2d import *

open_canvas()

background = load_image('background.png')
character = load_image('animation_sheet_hw.png')

walk_frames = [
    (45,  785, 120, 210),
    (225, 785, 150, 210),
    (415, 782, 145, 215),
    (600, 782, 155, 215),
    (785, 782, 165, 215),
    (995, 785, 135, 210)
]

run_frames = [
    (45,   530, 160, 220),
    (230,  530, 170, 220),
    (420,  530, 160, 220),
    (605,  528, 155, 225),
    (775,  525, 180, 230),
    (975,  528, 160, 225),
    (1160, 530, 170, 220),
    (1355, 530, 160, 220)
]

jump_frames = [
    (45,  260, 125, 165),
    (255, 280, 165, 200),
    (480, 325, 170, 190),
    (685, 300, 170, 180),
    (940, 260, 165, 165)
]

attack_frames = [
     (44,   25, 151, 196),
    (255,  23, 136, 232),
    (449,  23, 290, 203),
    (739,  26, 175, 194),
    (943,  26, 185, 187),
    (1150, 25, 205, 196),
    (1356, 25, 150, 196)
]

while True:

    frame = 0

    for x in range(100, 700, 5):
     clear_canvas()
     background.draw(400, 300, 800, 600)
     wx, wy, ww, wh = walk_frames[frame]
     character.clip_draw(wx, wy, ww, wh, x, 300, 85, 150)
     update_canvas()
     frame = (frame + 1) % 6
     delay (0.05)

    for x in range (700, 100, -5):
     clear_canvas()
     background.draw(400, 300, 800, 600)
     wx, wy, ww, wh = walk_frames[frame]
     character.clip_composite_draw(wx, wy, ww, wh, 0, 'h', x, 300, 85, 150)
     update_canvas()
     frame = (frame + 1) % 6
     delay(0.05)

    frame = 0

    for x in range(100, 700, 10):
     clear_canvas()
     background.draw(400, 300, 800, 600)
     rx, ry, rw, rh = run_frames[frame]
     character.clip_draw(rx, ry, rw, rh, x, 300, 110, 150)
     update_canvas()
     frame = (frame + 1) % 8
     delay(0.05)

    for x in range(700, 400, -10):
     clear_canvas()
     background.draw(400, 300, 800, 600)
     rx, ry, rw, rh = run_frames[frame]
     character.clip_composite_draw(rx, ry, rw, rh, 0, 'h', x, 300, 110, 150)
     update_canvas()
     frame = (frame + 1) % 8
     delay(0.05)

    jump_y = [300, 360, 420, 360, 300]

    for frame in range(5):
     clear_canvas()
     background.draw(400, 300, 800, 600)
     jx, jy, jw, jh = jump_frames[frame]
     character.clip_draw(jx, jy, jw, jh, 400, jump_y[frame], 110, 150)
     update_canvas()
     delay(0.15)

    for frame in range(7):
     clear_canvas()
     background.draw(400, 300, 800, 600)
     ax, ay, aw, ah = attack_frames[frame]
     character.clip_draw(ax, ay, aw, ah, 400, 300, 200, 170)
     update_canvas()
     delay(0.12)


close_canvas()