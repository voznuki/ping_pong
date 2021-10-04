from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

background = "background.png"
win_widht = 600
win_height = 500
back = transform.scale(image.load(background), (win_widht, win_height))
window = display.set_mode((win_widht, win_height))
window.blit(back, (0, 0))

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("racket.png", 30, 200, 4, 50, 120)
racket2 = Player("racket.png", 520, 200, 4, 50, 120)
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

ball_speed_x = ball.speed
ball_speed_y = ball.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(back, (0, 0))
        racket1.update_l()
        racket2.update_r()

        ball.reset()
        ball.rect.x += ball_speed_x 
        ball.rect.y += ball_speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            ball_speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_widht:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()

    display.update()
    clock.tick(FPS)