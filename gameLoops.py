import pygame


def run_event_loop(time_to_sleep, draw_info, event_list, in_game_mode):
    for event in event_list:
        if event.type == pygame.QUIT:
            in_game_mode.game_is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                draw_info = not draw_info
            elif event.key == pygame.K_DOWN:
                time_to_sleep += 0.01
            elif event.key == pygame.K_UP:
                time_to_sleep -= 0.01
                if time_to_sleep < 0:
                    time_to_sleep = 0
    return draw_info, time_to_sleep
