# Simple pygame program

# Import and initialize the pygame library
import pygame
from storeDisplay import StoreDisplay

def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)

ANIMATION_IMAGE_COUNT = 0
BOTTOM_BUTTON_ROW_HEIGHT = 900
class CookieClicker:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode([1000, 1000])
        # Start in the cookie screenstate
        self.screenState = "cookie"
        # Set clickCount to zero
        self.clickCount = 0
        # Set the current animanation to 0 (will load cookie 0)
        self.curClickAnimationCount = 0
        self.calculateClickCount()
        # w, h =
        self.storeDisplay = StoreDisplay((self.screen.get_size()[0], BOTTOM_BUTTON_ROW_HEIGHT))
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

            cookieButton = Buttonify("./images/footer/cookie.png", (250,BOTTOM_BUTTON_ROW_HEIGHT), self.screen)
            storeButton = Buttonify("./images/footer/store.png", (450,BOTTOM_BUTTON_ROW_HEIGHT), self.screen)
            statsButton = Buttonify("./images/footer/stats.png", (625,BOTTOM_BUTTON_ROW_HEIGHT), self.screen)
            settingsButton = Buttonify("./images/footer/settings.png", (900,BOTTOM_BUTTON_ROW_HEIGHT), self.screen)

            if (self.screenState == "cookie"):
                self.screen.blit(self.clickAnimation(), (0,0,1,10))

                self.screen.blit(self.cookieClickerText, self.clickCountRectangle)
            elif (self.screenState == "settings"):
                print("settings")
            elif (self.screenState == "stats"):
                print("stats")
            elif (self.screenState == "store"):
                print("store")
                self.storeDisplay.show(self.screen)

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    if (self.screenState == "cookie"):
                        if self.image.get_rect().collidepoint(x, y):
                            self.clickCount += 1
                            self.calculateClickCount()
                            self.curClickAnimationCount = ANIMATION_IMAGE_COUNT

                    if (self.screenState == "store"):
                        self.storeDisplay.updateScrollLocation(event)

                    if cookieButton[1].collidepoint(x, y):
                        self.screenState = "cookie"

                    if settingsButton[1].collidepoint(x, y):
                        self.screenState = "settings"

                    if statsButton[1].collidepoint(x, y):
                        self.screenState = "stats"

                    if storeButton[1].collidepoint(x, y):
                        self.screenState = "store"

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
