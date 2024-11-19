import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x_cord = 0
        y_cord = 0
        click_cord = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_cord = event.pos
                    if (0 <= click_cord[0] - x_cord < 32) and (0 <= click_cord[1] - y_cord < 32):
                        x_cord = (32 * (random.randrange(0, 20)))
                        y_cord = (32 * (random.randrange(0, 16)))


            screen.fill("light green")
            for i in range(20):
                x = 32 * (i + 1)
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for i in range(16):
                x = 32 * (i + 1)
                pygame.draw.line(screen, "black", (0, x), (640, x))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_cord, y_cord)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
