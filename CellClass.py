import pygame
from enum import Enum

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
    CELL_TYPES = Enum( 'CELL_TYPES', 'STATIC NORM' )
    STATIC_LIFESPAN = 175

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = False
        self.flag = False
        self.owner = cellSprite.NONE
        self.owner_color = cellSprite.COLOR_DEAD
        self.cell_type = cellSprite.CELL_TYPES.NORM
        self.life_span = -1
        self.x_pos = x
        self.y_pos = y
        self.num_nbrs = 0
        
        self.image = pygame.Surface( (cellSprite.WIDTH, cellSprite.HEIGHT) )
        self.image.fill( cellSprite.COLOR_DEAD )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def revive( self, owner, color, c_type ):
        self.alive = True
        self.owner = owner
        self.owner_color = color
        self.cell_type = c_type
        if c_type == cellSprite.CELL_TYPES.STATIC:
            self.lifespan = cellSprite.STATIC_LIFESPAN
        self.image.fill( color )

    def is_alive( self ):
        return self.alive

    def kill( self ):
        self.alive = False
        self.cell_type = cellSprite.CELL_TYPES.NORM
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

    def get_owner( self ):
        return self.owner

    def get_rect( self ):
        return self.rect

    def get_type( self ):
        return self.cell_type

    def count_nbrs(self, neighbors):
        self.num_nbrs = 0
        type_stat = cellSprite.CELL_TYPES.STATIC

        for cell in neighbors:
            if cell.is_alive() and cell.get_type() != type_stat:
                self.num_nbrs += 1

    def update( self ):
        # game rules
        if self.cell_type == cellSprite.CELL_TYPES.NORM:
            if self.alive == True:
                if self.num_nbrs < 2:
                        self.kill()
                elif self.num_nbrs > 3:
                        self.kill()
            else:
                if self.num_nbrs == 3:
                        self.revive( cellSprite.NONE, cellSprite.COLOR_ALIVE, cellSprite.CELL_TYPES.NORM )
        elif self.cell_type == cellSprite.CELL_TYPES.STATIC:
            if self.lifespan > 0:
                self.lifespan -= 1
            else:
                self.kill()

        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
