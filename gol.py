import pygame, sys, time
import CellClass, CapCellGameClass
from pygame.locals import *

def main():

    pygame.init()

    WHITE = ( 255, 255, 255 )
    GREY = ( 190, 190, 190 )
    BLACK = ( 0, 0, 0 )

    capCellGame = CapCellGameClass.CapCellGame()
    screen_height = capCellGame.get_screen_height()
    screen_width = capCellGame.get_screen_width()
    frame_delay = 0.02

    winSurface = pygame.display.set_mode( (screen_width, screen_height), 0, 32 )
    pygame.display.set_caption( 'Capture the Cell' )

    basicFont = pygame.font.SysFont( None, 25 )
    text_start = basicFont.render( 'START', 0, BLACK, GREY )
    text_start_rect = text_start.get_rect()
    text_start_rect.bottomleft = winSurface.get_rect().bottomleft
    
    text_stop = basicFont.render( 'STOP', 0, BLACK, GREY )
    text_stop_rect = text_stop.get_rect()
    text_stop_rect.bottomleft = winSurface.get_rect().bottomleft

    text_gen = basicFont.render( 'GEN: ' + str( capCellGame.get_gen() ), 0, BLACK, GREY )
    text_gen_rect = text_gen.get_rect()
    text_gen_rect.midbottom = winSurface.get_rect().midbottom

    while True:

        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if capCellGame.get_round_state() == False:
                    if text_start_rect.collidepoint( pos ):
                        capCellGame.start_round()
                    capCellGame.select_cell( pos )
                else:
                    if text_stop_rect.collidepoint( pos ):
                        capCellGame.end_round()

        capCellGame.update()

        winSurface.fill( GREY )
        if capCellGame.get_round_state() == True:
            winSurface.blit( text_stop, text_stop_rect )
        else:
            winSurface.blit( text_start, text_start_rect )
        text_gen = basicFont.render( 'GEN: ' + str( capCellGame.get_gen() ), 0, BLACK, GREY )
        winSurface.blit( text_gen, text_gen_rect )
        capCellGame.draw_cells( winSurface )

        time.sleep(frame_delay)
        pygame.display.update()

main()
