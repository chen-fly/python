import pygame
import time

def main():
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 600), 0, 32)

    #2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #3.创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")

    #3.把背景图片放到窗口中显示
    while True:

        #设定需要显示的背景图
        screen.blit(background, (0,0))

        screen.blit(hero, (230,400))

        #更改需要显示的内容
        pygame.display.update()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
