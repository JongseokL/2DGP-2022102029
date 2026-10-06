from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
CHARACTER_SIZE = 100
CHARACTER_HALF = CHARACTER_SIZE // 2


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y, facing_right

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                facing_right = True
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                facing_right = False
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
facing_right = True

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    moving = dir_x != 0 or dir_y != 0
    if moving:
        animation_y = 100 if facing_right else 0
    else:
        animation_y = 300 if facing_right else 200
    character.clip_draw(
        frame * CHARACTER_SIZE, animation_y,
        CHARACTER_SIZE, CHARACTER_SIZE, x, y
    )
    update_canvas()

    handle_events()
    x += dir_x * 5
    y += dir_y * 5
    x = max(CHARACTER_HALF, min(TUK_WIDTH - CHARACTER_HALF, x))
    y = max(CHARACTER_HALF, min(TUK_HEIGHT - CHARACTER_HALF, y))
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
