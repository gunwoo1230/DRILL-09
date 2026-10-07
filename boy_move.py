from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
FRAME_SIZE = 100
SPEED = 10
# 스프라이트 실제 몸 크기 기준 여백
MARGIN_X, MARGIN_Y = 35, 42
# animation_sheet 행의 bottom 값
IDLE_RIGHT, IDLE_LEFT, RUN_RIGHT, RUN_LEFT = 300, 200, 100, 0


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
    global frame, x, y, face
    frame = (frame + 1) % 8
    x += dir_x * SPEED
    y += dir_y * SPEED
    x = clamp(MARGIN_X, x, TUK_WIDTH - MARGIN_X)
    y = clamp(MARGIN_Y, y, TUK_HEIGHT - MARGIN_Y)
    if dir_x != 0:
        face = dir_x


def get_action_row():
    moving = dir_x != 0 or dir_y != 0
    if moving:
        return RUN_RIGHT if face == 1 else RUN_LEFT
    return IDLE_RIGHT if face == 1 else IDLE_LEFT


def draw():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * FRAME_SIZE, get_action_row(), FRAME_SIZE, FRAME_SIZE, x, y)
    update_canvas()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
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
