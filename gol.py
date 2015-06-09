import pygame, sys, time
import CapCellGameClass
from pygame.locals import *
from CellClass import cellSprite

def main():

    pygame.init()

    WHITE = ( 255, 255, 255 )
    GREY = ( 190, 190, 190 )
    BLACK = ( 0, 0, 0 )
    RED = ( 255, 0, 0 )
    YELLOW = ( 255, 255, 0 )

    P1_WIN = 'Player One Wins!'
    P2_WIN = 'Player Two Wins!'

    capCellGame = CapCellGameClass.CapCellGame()
    screen_height = capCellGame.get_screen_height()
    screen_width = capCellGame.get_screen_width()
    frame_delay = 0.005

    winSurface = pygame.display.set_mode( (screen_width, screen_height), 0, 32 )
    pygame.display.set_caption( 'Capture the Cell' )

    # set texts used in game
    basicFont = pygame.font.SysFont( None, 25 )
    text_start = basicFont.render( 'START', 0, BLACK, GREY )
    text_start_rect = text_start.get_rect()
    text_start_rect.bottomleft = winSurface.get_rect().bottomleft
    
    text_gen = basicFont.render( 'GEN: ' + str( capCellGame.get_gen() ), 0, BLACK, GREY )
    text_gen_rect = text_gen.get_rect()
    text_gen_rect.midbottom = winSurface.get_rect().midbottom
    
    text_round = basicFont.render( 'ROUND: ' + str( capCellGame.get_round() ), 0, BLACK, GREY )
    text_round_rect = text_round.get_rect()
    text_round_rect.bottomright = winSurface.get_rect().bottomright
    
    text_prompt_p1 = basicFont.render( 'PLAYER ONE: Place Cells', 0, BLACK, GREY )
    text_prompt_p1_rect = text_prompt_p1.get_rect()
    text_prompt_p1_rect.topleft = winSurface.get_rect().topleft
    
    text_prompt_p2 = basicFont.render( 'PLAYER TWO: Place Cells', 0, BLACK, GREY )
    text_prompt_p2_rect = text_prompt_p2.get_rect()
    text_prompt_p2_rect.topleft = winSurface.get_rect().topleft
    
    text_done = basicFont.render( 'DONE', 0, BLACK, GREY )
    text_done_rect = text_done.get_rect()
    text_done_rect.topright = winSurface.get_rect().topright

    game_over = capCellGame.is_game_over()


	# Game loop
    while True:

        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if capCellGame.in_round() == False:
                    if text_start_rect.collidepoint( pos ):
                        capCellGame.start_round()
                    if text_done_rect.collidepoint( pos ):
                        if capCellGame.get_turn_p1() == True:
                            capCellGame.set_turn_p1()
                            capCellGame.set_turn_p2()
                        else:
                            capCellGame.set_turn_p2()
                    if pygame.mouse.get_pressed()[0]:
                    	capCellGame.select_cell( pos, cellSprite.CELL_TYPES.NORM )
                    elif pygame.mouse.get_pressed()[2]:
                    	capCellGame.select_cell( pos, cellSprite.CELL_TYPES.STATIC )

        capCellGame.update()
        game_over = capCellGame.is_game_over()

		# draw new frame based on game state
        winSurface.fill( GREY )
        if game_over != True:
            if capCellGame.in_round() != True:
                if capCellGame.get_turn_p1() == True:
                    winSurface.blit( text_prompt_p1, text_prompt_p1_rect )
                    winSurface.blit( text_done, text_done_rect )
                elif capCellGame.get_turn_p2() == True:
                    winSurface.blit( text_prompt_p2, text_prompt_p2_rect )
                    winSurface.blit( text_done, text_done_rect )
                else:
                    winSurface.blit( text_start, text_start_rect )

        text_gen = basicFont.render( 'GEN: ' + str( capCellGame.get_gen() ), 0, BLACK, GREY )
        winSurface.blit( text_gen, text_gen_rect )
        
        text_round = basicFont.render( 'ROUND: ' + str( capCellGame.get_round() ), 0, BLACK, GREY )
        winSurface.blit( text_round, text_round_rect )

        capCellGame.draw_cells( winSurface )

        if game_over == True:
            winFont = pygame.font.SysFont( None, 45 )
            text_win = winFont.render( str( capCellGame.get_winner() ), 0, YELLOW, None )
            text_win_rect = text_win.get_rect()
            text_win_rect.center = winSurface.get_rect().center
            winSurface.blit( text_win, text_win_rect )

        time.sleep(frame_delay)
        pygame.display.update()

main()
