from pygame import *


clock = time.Clock()
window_h = 500
window_w = 800

window = display.set_mode((window_w, window_h))

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0,255,255))

    display.update()

    clock.tick(60)
