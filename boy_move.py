from pico2d import *


def handle_events():
    print('handle_events')


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
