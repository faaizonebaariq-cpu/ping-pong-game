from pygame import *

win_width = 1000
win_height = 558
img_back = "table.jpg"

window = display.set_mode((win_width, win_height))
display.set_caption('ping pong game')
background = transform.scale(image.load(img_back), (win_width, win_height))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed


batman = Player('bat.png', 30, win_height//2, 4)
batman2 = Player2('bat.png', win_width-100, win_height//2, 4)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0, 0))   

    batman.update()
    batman2.update()
    batman.reset()
    batman2.reset()

    display.update()
    clock.tick(FPS)
