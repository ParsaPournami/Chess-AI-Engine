import pygame
import sys
from setting import Config
from screens.menu import Menu

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(Config.resolution)

    loaded_icon = pygame.image.load("./assets/images/white_knight.png")
    main_icon = pygame.transform.smoothscale(loaded_icon, (Config.windowIconSize, Config.windowIconSize))
    pygame.display.set_icon(main_icon)
    # game loop
    MenuScreen = Menu(screen)
    MenuScreen.Run()
    # quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
