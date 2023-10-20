import pygame

import gameLoops
import gamemode


def test_event_loop_positive_time_to_sleep():
    current_time_to_sleep = 0
    mocked_game_mode = gamemode.GameMode()
    mocked_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_DOWN})
    returned_time_to_sleep, not_used_draw_info = gameLoops.run_event_loop(current_time_to_sleep, True, [mocked_event], mocked_game_mode)
    assert returned_time_to_sleep > current_time_to_sleep


def test_event_loop_negative_time_to_sleep():
    current_time_to_sleep = 0
    mocked_game_mode = gamemode.GameMode()
    mocked_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_UP})
    returned_time_to_sleep, not_used_draw_info = gameLoops.run_event_loop(current_time_to_sleep, True, [mocked_event], mocked_game_mode)
    assert returned_time_to_sleep > current_time_to_sleep


def test_event_loop_quit():
    mocked_game_mode = gamemode.GameMode()
    mocked_event = pygame.event.Event(pygame.QUIT, {"key": pygame.K_ESCAPE})
    not_used_time_to_sleep, not_used_draw_info = gameLoops.run_event_loop(0, True, [mocked_event], mocked_game_mode)
    assert mocked_game_mode.game_is_running is False
