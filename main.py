from pygame import *


clock = time.Clock()
window_h = 500
window_w = 800

window = display.set_mode((window_w, window_h))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(30, 200))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < window_h - 65:
            self.rect.y += 5


player = Player("racket.png", 50, 300, 10)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0,255,255))

    player.update()
    player.reset()


    display.update()

    clock.tick(60)
