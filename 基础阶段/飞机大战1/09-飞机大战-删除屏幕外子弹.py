import pygame
from pygame.locals import *
import time

class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 450
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []#储存发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in  self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move(self, direction):
        if direction == "left":
            self.x -= 5
        elif direction == "right":
            self.x += 5
        elif direction == "up":
            pass
        elif direction == "down":
            pass

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.falg = "right"
        self.x = 210
        self.y = 10
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.bullet_list = []#储存发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    #    for bullet in  self.bullet_list:
    #        bullet.display()
    #        bullet.move()

    def auto_move(self):
        if self.falg == "right":
            if self.x<430:
                self.x += 5
            else:
                self.falg = "left"
        else:
            if self.x>0:
                self.x -= 5
            else:
                self.falg = "right"

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y<300:
            return True
        else:
            return False

def key_control(obj):
    #获取事件，比如按键等
    for event in pygame.event.get():
        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                obj.move("left")
                print("left")
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                obj.move("right")
                print("right")
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print("space")
                obj.fire()
            #    print(len(obj.bullet_list))




def main():
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 600), 0, 32)

    #2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #3.创建一个飞机图片
    hero = HeroPlane(screen)

    #创建一个敌机
    enemy = EnemyPlane(screen)

    #3.把背景图片放到窗口中显示
    while True:

        #设定需要显示的背景图
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.auto_move()#敌机自动移动

        #更改需要显示的内容
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
