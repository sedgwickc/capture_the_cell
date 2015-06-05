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

    P1_SELECT = 'PLAYER ONE: Select Cells'
    P2_SELECT = 'PLAYER TWO: Select Cells'
    ROUND = 'ROUND #'
    ROUND_LEN = 50 # number of generations per round

    COLOR_DEAD = BLACK
    COLOR_ALIVE = GREEN
    COLOR_FLAG_P1 = BLUE
    COLOR_FLAG_P2 = PURPLE
    
    GRID_HEIGHT = 50
    GRID_WIDTH = 50
    BAR_TOP = 30
    BAR_BOTTOM = 50
    MARGIN = 1

    NONE = 0
    P_ONE = 1
    P_TWO = 2
    P1_COLOR = BLUE
    P2_COLOR = PURPLE

    def __init__(self):
        
        self.game_over = False
        self.in_rnd = False
        self.turn_p1 = True
        self.turn_p2 = False
        self.winner = CapCellGame.NONE
        self.score_p1 = 0
        self.score_p2 = 0
        self.gen = 1
        self.gen_start = 1
        self.round_num = 1

        self.grid_height = CapCellGame.GRID_HEIGHT
        self.grid_width = CapCellGame.GRID_WIDTH
        self.margin = CapCellGame.MARGIN

        self.cell_grid = []
        self.cells = pygame.sprite.Group()

        cell_y = CapCellGame.BAR_TOP
        for i in range( 0, self.grid_height ):
            self.cell_grid.append( [] )
            cell_x = 2
            for j in range( 0, self.grid_width ):
                new_cell = CellClass.cellSprite(cell_x, cell_y)
                self.cell_grid[i].append( new_cell )
                self.cells.add( new_cell )
                cell_x += CellClass.cellSprite.WIDTH + self.margin
            cell_y += CellClass.cellSprite.HEIGHT + self.margin

        # set player flags, turn into function!
        self.flag_p1 = []
        self.flag_p1.append(self.cell_grid[CapCellGame.GRID_WIDTH-2][CapCellGame.GRID_HEIGHT-2])
        self.flag_p1.append(self.cell_grid[CapCellGame.GRID_WIDTH-2][CapCellGame.GRID_HEIGHT-3])
        self.flag_p1.append(self.cell_grid[CapCellGame.GRID_WIDTH-3][CapCellGame.GRID_HEIGHT-2])
        self.flag_p1.append(self.cell_grid[CapCellGame.GRID_WIDTH-3][CapCellGame.GRID_HEIGHT-3])
        for cell in self.flag_p1:
            cell.set_flag(CapCellGame.P_ONE, CapCellGame.P1_COLOR)

        self.flag_p2 = []
        self.flag_p2.append(self.cell_grid[1][1])
        self.flag_p2.append(self.cell_grid[1][2])
        self.flag_p2.append(self.cell_grid[2][1])
        self.flag_p2.append(self.cell_grid[2][2])
        for cell in self.flag_p2:
            cell.set_flag(CapCellGame.P_TWO, CapCellGame.P2_COLOR)

    def get_screen_height( self ):
        height = self.grid_height * (CellClass.cellSprite.HEIGHT + self.margin) 
        height += CapCellGame.BAR_TOP
        height += CapCellGame.BAR_BOTTOM
        return height
    
    def get_screen_width( self ):
        return self.grid_width * (CellClass.cellSprite.WIDTH + self.margin) + 2 * self.margin

    def get_gen( self ):
        return self.gen

    def get_round( self ):
        return self.round_num

    def get_cells( self ):
        return self.cells

    def in_round( self ):
        return self.in_rnd

    def get_winner( self ):
        return self.winner

    def get_turn_p1( self ):
        return self.turn_p1

    def set_turn_p1( self ):
        if self.turn_p1 == True:
            self.turn_p1 = False
        else:
            self.turn_p1 = True

    def get_turn_p2( self ):
        return self.turn_p2

    def set_turn_p2( self ):
        if self.turn_p2 == True:
            self.turn_p2 = False
        else:
            self.turn_p2 = True

    def start_round( self ):
        self.gen_start = self.gen
        self.in_rnd = True

    def end_round( self ):
        self.in_rnd = False
        self.turn_p1 = True
        self.turn_p2 = False

    def is_game_over( self ):
        return self.game_over
   
    def select_cell( self, pos ):
        for cell in self.cells:
            if cell.get_rect().collidepoint( pos ):
                if cell.is_alive():
                    cell.kill()
                else:
                    if self.turn_p1 == True:
                        cell.revive(CapCellGame.P_ONE, CapCellGame.P1_COLOR)
                    else:
                        cell.revive(CapCellGame.P_TWO, CapCellGame.P2_COLOR)

    def draw_cells( self, surface ):
        self.cells.draw( surface )

    def update( self ):

        if len(self.flag_p1) == 0:
            self.winner = 'Player 2 Wins!'
            self.game_over = True
        elif len(self.flag_p2) == 0:
            self.winner = 'Player 1 Wins!'
            self.game_over = True

        if self.in_rnd != False and self.gen <= (self.gen_start + CapCellGame.ROUND_LEN):
            self.gen += 1
            self.round_num = self.gen // CapCellGame.ROUND_LEN

            if self.gen >= self.gen_start + CapCellGame.ROUND_LEN:
                self.end_round()

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
            for cell in self.flag_p1:
                if cell.is_alive() == False:
                    self.flag_p1.remove( cell )
            for cell in self.flag_p2:
                if cell.is_alive() == False:
                    self.flag_p2.remove( cell )
