import pygame

class cellSprite( pygame.sprite.Sprite ):
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (200, 0, 200)
    
    COLOR_DEAD = BLACK
    COLOR_ALIVE = GREEN
    
    HEIGHT = 10
    WIDTH = 10
    FONT_DEBUG = 10

    NONE = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = False
        self.flag = False
        self.owner = cellSprite.NONE
        self.owner_color = cellSprite.COLOR_ALIVE
        self.x_pos = x
        self.y_pos = y
        self.num_nbrs = 0
        
        self.image = pygame.Surface( (cellSprite.WIDTH, cellSprite.HEIGHT) )
        self.image.fill( cellSprite.COLOR_DEAD )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def revive( self, owner, color ):
        self.alive = True
        self.owner = owner
        self.owner_color = color
        self.image.fill( color )

    def is_alive( self ):
        return self.alive

    def kill( self ):
        self.alive = False
        self.owner = cellSprite.NONE
        self.image.fill( cellSprite.COLOR_DEAD )

    def is_flag( self ):
        return self.flag

    def set_flag( self, player, color ):
        self.flag = True
        self.alive = True
        self.image.fill( color )
        self.owner = player

    def set_owner( self, player ):
        self.owner = player

    def get_rect( self ):
        return self.rect

    def count_nbrs(self, neighbors):
        self.num_nbrs = 0
        for cell in neighbors:
            if cell.is_alive():
                self.num_nbrs += 1

    def update( self ):
        # game rules
        if self.alive == True:
            if self.num_nbrs < 2:
                    self.kill()
            elif self.num_nbrs > 3:
                    self.kill()
        else:
            if self.num_nbrs == 3:
                    self.revive( cellSprite.NONE, cellSprite.COLOR_ALIVE )

        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
