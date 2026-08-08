from pygame import *
from random import randint

win_width = 1000
win_height = 558
img_back = "table.jpg"

window = display.set_mode((win_width, win_height))
display.set_caption('ping pong game')
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0, 0))

    display.update()
    time.delay(50)

