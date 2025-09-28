from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size1, size2, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1, size2))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed


win_width = 600
win_height = 500
back = (200, 200, 255)

window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
window.fill(back)

game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)

   
