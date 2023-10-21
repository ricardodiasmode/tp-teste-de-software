import time
import pygame
import gamemode
from gameLoops import run_event_loop, run_game_loop

# Basic game setups
pygame.init()
clock = pygame.time.Clock()
game_mode = gamemode.GameMode()
game_mode.reset_game()
pygame.display.update()
should_draw_info = False
sleep_time = 0.0

while game_mode.game_is_running:
    should_draw_info, sleep_time = run_event_loop(sleep_time, should_draw_info, pygame.event.get(), game_mode)
    run_game_loop(game_mode)

    if should_draw_info:
        game_mode.draw_info()

    time.sleep(sleep_time)

    game_mode.on_turn_end()

    pygame.display.update()
    clock.tick()
