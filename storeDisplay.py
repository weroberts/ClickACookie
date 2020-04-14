import pygame

class StoreDisplay:
    def __init__(self, surface):
        self.surfaceWidth, self.surfaceHeight = surface
        self.parent = pygame.surface.Surface(surface)
        self.child = pygame.surface.Surface((self.surfaceWidth, 1500))

        self.scroll_y = 1
        pygame.draw.rect(self.child,(0,0,255),(0,0,self.surfaceWidth,150))



    # Show the store display
    def show(self, screen):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GeeksForaoijf djav jdfksaj fkdjsakl fjdlksaj flkdjsalk fjdslakj fkldsaj fkldjsalk fjdlskaj fldksjal kfdjsak fjdskla fldk saGeeks', True, green, blue)
        textRect = text.get_rect()

        self.child.blit(text, textRect)

        self.parent.blit(self.child, (0, self.scroll_y))
        screen.blit(self.parent, (0, 0))

    # Update the scroll location.
    # This method receives an event from
    def updateScrollLocation(self, event):
        if event.button == 4: self.scroll_y = min(self.scroll_y + 15, 0)
        if event.button == 5: self.scroll_y = max(self.scroll_y - 15, -300)
