import pygame
import CellClass

class CapCellGame():
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (200, 0, 200)
    
    NONE = 0
    P_ONE = 1
    P_TWO = 2
    

    COLOUR_DEAD = BLACK
    COLOUR_ALIVE = GREEN
    COLOUR_FLAG_P1 = BLUE
    COLOUR_FLAG_P2 = PURPLE
    
    GRID_HEIGHT = 50
    GRID_WIDTH = 50
    MENU_HEIGHT = 40
    MARGIN = 1

    NONE = 0
    P_ONE = 1
    P_TWO = 2

    def __init__(self):
        
        self.game_over = False
        self.start = False
        self.turn_p1 = False
        self.turn_p2 = False
        self.cur_turn = CapCellGame.P_ONE
        self.winner = CapCellGame.NONE
        self.score_p1 = 0
        self.score_p2 = 0
        self.gen = 0

        self.grid_height = CapCellGame.GRID_HEIGHT
        self.grid_width = CapCellGame.GRID_WIDTH
        self.margin = CapCellGame.MARGIN

        self.cell_grid = []
        self.cells = pygame.sprite.Group()

        cell_y = 2
        for i in range( 0, self.grid_height ):
                self.cell_grid.append( [] )
                cell_x = 2
                for j in range( 0, self.grid_width ):
                    new_cell = CellClass.cellSprite(cell_x, cell_y)
                    self.cell_grid[i].append( new_cell )
                    self.cells.add( new_cell )
                    cell_x += CellClass.cellSprite.WIDTH + self.margin
                cell_y += CellClass.cellSprite.HEIGHT + self.margin

    def get_screen_height( self ):
        return self.grid_height * (CellClass.cellSprite.HEIGHT + self.margin) + CapCellGame.MENU_HEIGHT
    
    def get_screen_width( self ):
        return self.grid_width * (CellClass.cellSprite.WIDTH + self.margin) + 2 * self.margin

    def get_gen( self ):
        return self.gen

    def get_cells( self ):
        return self.cells

    def get_round_state( self ):
        return self.start

    def start_round( self ):
        self.start = True

    def end_round( self ):
        self.start = False
   
    def select_cell( self, pos ):
        for cell in self.cells:
            if cell.get_rect().collidepoint( pos ):
                if cell.is_alive():
                    cell.kill()
                else:
                    cell.revive()

    def draw_cells( self, surface ):
        self.cells.draw( surface )

    def update( self ):
        if self.turn_p1 == True:
            self.turn_p1 = False
            # player 1 sets flag

        if self.turn_p2 == True:
            self.turn_p2 = True

        if self.start != False:
            self.gen += 1
            for i in range( 0, self.grid_height ):
                for j in range( 0, self.grid_width ):
                    neighbors = [] 
                    if i == 0:
                        if j == 0:
                            neighbors.append( self.cell_grid[i][j+1] ) 
                            neighbors.append( self.cell_grid[i+1][j] )
                            neighbors.append( self.cell_grid[i+1][j+1] )
                        elif j < self.grid_width - 1:
                            neighbors.append( self.cell_grid[i][j-1] )
                            neighbors.append( self.cell_grid[i][j+1] )
                            neighbors.append( self.cell_grid[i+1][j] )
                            neighbors.append( self.cell_grid[i+1][j+1] )
                            neighbors.append( self.cell_grid[i+1][j-1] )
                        else:
                            neighbors.append( self.cell_grid[i][j-1] )
                            neighbors.append( self.cell_grid[i+1][j] )
                            neighbors.append( self.cell_grid[i+1][j-1] )
                    elif i < self.grid_height - 1:
                        if j == 0:
                            neighbors.append( self.cell_grid[i+1][j] ) 
                            neighbors.append( self.cell_grid[i-1][j] ) 
                            neighbors.append( self.cell_grid[i][j+1] )
                            neighbors.append( self.cell_grid[i+1][j+1] )
                            neighbors.append( self.cell_grid[i-1][j+1] )
                        elif j < self.grid_width - 1:
                            neighbors.append( self.cell_grid[i][j-1] )
                            neighbors.append( self.cell_grid[i][j+1] )
                            neighbors.append( self.cell_grid[i+1][j] )
                            neighbors.append( self.cell_grid[i-1][j] )
                            neighbors.append( self.cell_grid[i+1][j+1] )
                            neighbors.append( self.cell_grid[i-1][j+1] )
                            neighbors.append( self.cell_grid[i+1][j-1] )
                            neighbors.append( self.cell_grid[i-1][j-1] )
                        else:
                            neighbors.append( self.cell_grid[i][j-1] )
                            neighbors.append( self.cell_grid[i+1][j] )
                            neighbors.append( self.cell_grid[i+1][j-1] )
                            neighbors.append( self.cell_grid[i-1][j] )
                            neighbors.append( self.cell_grid[i-1][j-1] )
                    else:
                        if j == 0:
                            neighbors.append( self.cell_grid[i-1][j] ) 
                            neighbors.append( self.cell_grid[i][j+1] )
                            neighbors.append( self.cell_grid[i-1][j+1] )
                        elif j < self.grid_width - 1:
                            neighbors.append( self.cell_grid[i][j-1] )
                            neighbors.append( self.cell_grid[i][j+1] )
                            neighbors.append( self.cell_grid[i-1][j+1] )
                            neighbors.append( self.cell_grid[i-1][j] )
                            neighbors.append( self.cell_grid[i-1][j-1] )
                        else:
                            neighbors.append( self.cell_grid[i][j-1] )
                            neighbors.append( self.cell_grid[i-1][j] )
                            neighbors.append( self.cell_grid[i-1][j-1] )

                    self.cell_grid[i][j].count_nbrs( neighbors )
            self.cells.update()
