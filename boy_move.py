from pico2d import *


def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


def update():
    global frame, x, y
    frame = (frame + 1) % 8
    x += dir_x * 10
    y += dir_y * 10
    print(dir_x != 0 or dir_y != 0)


def draw():
    clear_canvas()
    tuk_ground.draw(640, 512)
    if dir_x != 0 or dir_y != 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif face == 1:
        character.clip_draw(frame * 100, 300, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 200, 100, 100, x, y)
    update_canvas()


open_canvas(1280, 1024)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
# animation_sheet 행(bottom): 300 IDLE 오른쪽, 200 IDLE 왼쪽, 100 RUN 오른쪽, 0 RUN 왼쪽

running = True
x, y = 640, 512
frame = 0
face = 1
dir_x = 0
dir_y = 0

while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()
