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
    def update(self, up, down):
        keys = key.get_pressed()

        if keys[up] and self.rect.y > self.speed:
            self.rect.y -= 5
        if keys[down] and self.rect.y < window_h - 200:
            self.rect.y += self.speed


player = Player("racket.png", 50, 300, 5)
player1 = Player("racket.png", (window_w - 50), 300, 5)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0,255,255))

    player.update(K_w, K_s)
    player.reset()

    player1.update(K_UP, K_DOWN)
    player1.reset()

    display.update()

    clock.tick(60)
