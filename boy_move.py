from pico2d import *


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update():
    pass


def draw():
    clear_canvas()
    tuk_ground.draw(640, 512)
    character.clip_draw(0, 300, 100, 100, 640, 512)
    update_canvas()


open_canvas(1280, 1024)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
# animation_sheet 행(bottom): 300 IDLE 오른쪽, 200 IDLE 왼쪽, 100 RUN 오른쪽, 0 RUN 왼쪽

running = True

while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()
