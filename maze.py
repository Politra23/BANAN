from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Aboba(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += 10
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 10
        if keys[K_d] and self.rect.x < 1100:
            self.rect.x += 10
        
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_height = wall_height
        self.wall_width = wall_width


        #св от родителя
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


wall1 = Wall(57,61,71, 100, 100, 50, 150)
wall2 = Wall(57,61,71, 200, 100, 30, 200)
wall3 = Wall(57,61,71, 500, 100, 300, 20)
wall4 = Wall(57,61,71, 500, 500, 300, 10)


class Alexander(GameSprite):
    direction = 'left'
    def move(self):
        if self.rect.x == 600:
            self.direction = 'left'
        if self.rect.x == 450:
            self.direction = 'right'

        if self.direction == 'left':
            self.rect.x -= 5
        else:
            self.rect.x += 5
          







#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


#Персонажи игры:
player = Aboba('hero.png', 5, win_height - 80, 4)
enemy = Alexander('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

run = True
game = True
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None, 100)
win = font.render('Вы победили!', True, (225, 215, 0))
lose = font.render('Вы проиграли!', True, (225, 215, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if run == True:
        window.blit(background,(0, 0)) 
        player.move()
        enemy.move()
        player.reset()
        enemy.reset()
        final.reset()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()

        

    if sprite.collide_rect(player, enemy) or \
        sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or \
            sprite.collide_rect(player, wall2):
        window.blit(lose, (600, 350))
        game = False
        #auch.play()
    if sprite.collide_rect(player, final):
        window.blit(win, (600, 350))
        game = False

    display.update()
    clock.tick(30)
