import pygame

class cellSprite( pygame.sprite.Sprite ):
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (200, 0, 200)
    
    COLOUR_DEAD = BLACK
    COLOUR_ALIVE = GREEN
    COLOUR_FLAG_P1 = BLUE
    COLOUR_FLAG_P2 = PURPLE
    
    HEIGHT = 10
    WIDTH = 10
    FONT_DEBUG = 10

    NONE = 0
    P_ONE = 1
    P_TWO = 2

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = False
        self.flag = False
        self.owner = cellSprite.NONE
        self.x_pos = x
        self.y_pos = y
        self.num_nbrs = 0
        
        self.image = pygame.Surface( (self.WIDTH, self.HEIGHT) )
        self.image.fill( self.COLOUR_DEAD )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def revive( self ):
        self.alive = True
        self.image.fill( self.COLOUR_ALIVE )

    def is_alive( self ):
        return self.alive

    def kill( self ):
        self.alive = False
        self.image.fill( self.COLOUR_DEAD )

    def is_flag( self ):
        return self.flag

    def set_flag( self, player ):
        if player == cellSprite.P_ONE:
            self.image.fill( cellSprite.COLOUR_FLAG_P1 )
            self.owner = player
        elif player == cellSprite.P_TWO:
            self.image.fill( cellSprite.COLOUR_FLAG_P2 )
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
                    self.alive = False
            elif self.num_nbrs > 3:
                    self.alive = False
        else:
            if self.num_nbrs == 3:
                    self.alive = True
        # update cell image     
        if self.alive == False:
            self.image.fill( self.COLOUR_DEAD )
        else:
            self.image.fill( self.COLOUR_ALIVE )
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
