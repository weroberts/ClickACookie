# Simple pygame program

# Import and initialize the pygame library
import pygame
ANIMATION_IMAGE_COUNT = 50
class CookieClicker:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode([1000, 1000])
        self.clickCount = 0
        self.curClickAnimationCount = 0
        self.calculateClickCount()
        # Run until the user asks to quit
        self.image = pygame.image.load('./images/cookie0.png')

    def clickAnimation(self):
        self.image = pygame.image.load('./images/cookie' + str(self.curClickAnimationCount) + '.png')
        if (self.curClickAnimationCount > 0):
            self.curClickAnimationCount -= 1
        return self.image

    def run(self):
        running = True
        while running:
            # Fill the background with white
            self.screen.fill((255, 255, 255))

            self.screen.blit(self.clickAnimation(), (0,0,1,10))

            self.screen.blit(self.cookieClickerText, self.clickCountRectangle)

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    if self.image.get_rect().collidepoint(x, y):
                        self.clickCount += 1
                        self.calculateClickCount()
                        self.curClickAnimationCount = ANIMATION_IMAGE_COUNT
                if event.type == pygame.QUIT:
                    running = False

            # Flip the display
            self.pygame.display.flip()

    def calculateClickCount(self):
        font = pygame.font.Font(None, 72)
        font_color = (0,0,0)
        font_background = (255,255,255)
        self.cookieClickerText = font.render(str(self.clickCount), True, font_color, font_background)
        self.clickCountRectangle = self.cookieClickerText.get_rect()
        self.clickCountRectangle.centerx, self.clickCountRectangle.centery = 100, 100

    def quit(self):
        # Done! Time to quit.
        self.pygame.quit()

cookieClicker = CookieClicker()
cookieClicker.run()
cookieClicker.quit()
