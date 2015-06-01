import pygame, sys, time
import CellClass
from pygame.locals import *

def main():

    pygame.init()

    WHITE = ( 255, 255, 255 )
    GREY = ( 190, 190, 190 )
    BLACK = ( 0, 0, 0 )
    screen_height = 650
    screen_width = 541
    grid_height = 50
    grid_width = 50
    margin = 1
    frame_delay = 0.02

    cell_grid = []
    cells = pygame.sprite.Group()

    cell_y = 2
    for i in range( 0, grid_height ):
        cell_grid.append( [] )
        cell_x = 2
        for j in range( 0, grid_width ):
            new_cell = CellClass.cellSprite(cell_x, cell_y)
            cell_grid[i].append( new_cell )
            cells.add( new_cell )
            cell_x += CellClass.cellSprite.WIDTH + margin
        cell_y += CellClass.cellSprite.HEIGHT + margin
    
    winSurface = pygame.display.set_mode( (screen_width, screen_height), 0, 32 )
    pygame.display.set_caption( 'Game of Life' )

    basicFont = pygame.font.SysFont( None, 25 )
    text_start = basicFont.render( 'START', 0, BLACK, GREY )
    text_start_rect = text_start.get_rect()
    text_start_rect.bottomleft = winSurface.get_rect().bottomleft
    
    gen = 0;
    text_gen = basicFont.render( 'GEN: ' + str( gen ), 0, BLACK, GREY )
    text_gen_rect = text_gen.get_rect()
    text_gen_rect.midbottom = winSurface.get_rect().midbottom

    text_stop = basicFont.render( 'STOP', 0, BLACK, GREY )
    text_stop_rect = text_stop.get_rect()
    text_stop_rect.bottomleft = winSurface.get_rect().bottomleft

    start = False

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start ==  False:
                    if text_start_rect.collidepoint( pos ):
                        start = True
                    for cell in cells:
                        if cell.get_rect().collidepoint( pos ):
                            if cell.is_alive():
                                cell.kill()
                            else:
                                cell.revive()
                else:
                    if text_stop_rect.collidepoint( pos ):
                        start = False

        if start != False:
            gen += 1
            for i in range( 0, grid_height ):
                for j in range( 0, grid_width ):
                    neighbors = [] 
                    if i == 0:
                        if j == 0:
                            neighbors.append( cell_grid[i][j+1] ) 
                            neighbors.append( cell_grid[i+1][j] )
                            neighbors.append( cell_grid[i+1][j+1] )
                        elif j < grid_width - 1:
                            neighbors.append( cell_grid[i][j-1] )
                            neighbors.append( cell_grid[i][j+1] )
                            neighbors.append( cell_grid[i+1][j] )
                            neighbors.append( cell_grid[i+1][j+1] )
                            neighbors.append( cell_grid[i+1][j-1] )
                        else:
                            neighbors.append( cell_grid[i][j-1] )
                            neighbors.append( cell_grid[i+1][j] )
                            neighbors.append( cell_grid[i+1][j-1] )
                    elif i < grid_height - 1:
                        if j == 0:
                            neighbors.append( cell_grid[i+1][j] ) 
                            neighbors.append( cell_grid[i-1][j] ) 
                            neighbors.append( cell_grid[i][j+1] )
                            neighbors.append( cell_grid[i+1][j+1] )
                            neighbors.append( cell_grid[i-1][j+1] )
                        elif j < grid_width - 1:
                            neighbors.append( cell_grid[i][j-1] )
                            neighbors.append( cell_grid[i][j+1] )
                            neighbors.append( cell_grid[i+1][j] )
                            neighbors.append( cell_grid[i-1][j] )
                            neighbors.append( cell_grid[i+1][j+1] )
                            neighbors.append( cell_grid[i-1][j+1] )
                            neighbors.append( cell_grid[i+1][j-1] )
                            neighbors.append( cell_grid[i-1][j-1] )
                        else:
                            neighbors.append( cell_grid[i][j-1] )
                            neighbors.append( cell_grid[i+1][j] )
                            neighbors.append( cell_grid[i+1][j-1] )
                            neighbors.append( cell_grid[i-1][j] )
                            neighbors.append( cell_grid[i-1][j-1] )
                    else:
                        if j == 0:
                            neighbors.append( cell_grid[i-1][j] ) 
                            neighbors.append( cell_grid[i][j+1] )
                            neighbors.append( cell_grid[i-1][j+1] )
                        elif j < grid_width - 1:
                            neighbors.append( cell_grid[i][j-1] )
                            neighbors.append( cell_grid[i][j+1] )
                            neighbors.append( cell_grid[i-1][j+1] )
                            neighbors.append( cell_grid[i-1][j] )
                            neighbors.append( cell_grid[i-1][j-1] )
                        else:
                            neighbors.append( cell_grid[i][j-1] )
                            neighbors.append( cell_grid[i-1][j] )
                            neighbors.append( cell_grid[i-1][j-1] )

                    cell_grid[i][j].count_nbrs( neighbors )
            cells.update()

        winSurface.fill( GREY )
        if start == True:
        	winSurface.blit( text_stop, text_stop_rect )
        else:
        	winSurface.blit( text_start, text_start_rect )
        text_gen = basicFont.render( 'GEN: ' + str( gen ), 0, BLACK, GREY )
        winSurface.blit( text_gen, text_gen_rect )
        cells.draw( winSurface )

        time.sleep(frame_delay)
        pygame.display.update()

main()
