from pico2d import *


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


def update():
    print('update')


def draw():
    print('draw')


open_canvas(1280, 1024)

running = True

while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()
