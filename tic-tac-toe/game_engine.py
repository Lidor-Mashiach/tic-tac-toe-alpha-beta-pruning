import time
import numpy as np
import minimax_tictacfive
import alpha_beta_tictacfive, heuristic_alpha_beta_tictacfive, heuristics
from game_state import game_state
from player_agent import player_agent, player_agent_heuristics


def print_current_state(curr_state, player_turn):
    print(f"Current player is player {player_turn},"
          f" last move was {curr_state.get_last_move()}."
          f"\nThe board is:\n"
          f"{curr_state.get_grid()}")


def print_result(curr_state):
    if curr_state.get_score() == 0:
        print(f"\n\n A draw!")
    else:
        print(f"\n\nPlayer {(curr_state.get_curr_player() % 2) + 1} is the winner!!")



def play_tictacfive(player_1, player_2, init_state):
    players = {1: player_1, 2: player_2}
    curr_player = player_1
    player_turn = 1
    curr_state = init_state
    print(f"start board is:\n{curr_state.get_grid()}")
    while not curr_state.is_terminal():
        chosen_move = curr_player.get_next_move(curr_state)
        curr_state.apply_move(chosen_move)
        print_current_state(curr_state, player_turn)
        player_turn = curr_state.get_curr_player()
        curr_player = players[player_turn]
    print_result(curr_state)


def play_with_minimax():
    player_1 = player_agent(minimax_tictacfive.maximin)
    player_2 = player_agent(minimax_tictacfive.minimax)
    game_state.set_winning_length(3)
    grid = np.zeros((3, 3), dtype=int)
    grid[1, 1] = 1
    grid[1, 0] = 2
    init_state = game_state(grid, 1, (1, 0), 2)
    play_tictacfive(player_1, player_2, init_state)


def play_with_alpha_beta():
    player_1 = player_agent(alpha_beta_tictacfive.alphabeta_max)
    player_2 = player_agent(alpha_beta_tictacfive.alphabeta_min)
    game_state.set_winning_length(3)
    grid = np.zeros((4, 4), dtype=int)
    grid[1, 1] = 1
    grid[2, 2] = 2
    init_state = game_state(grid, 1, (2, 2), 2)
    play_tictacfive(player_1, player_2, init_state)


def play_with_heuristics():
    depth_player_1 = 3
    depth_player_2 = 3

    # try different depths, you can change the depth numbers, board size and locations
    # depth_player_1 = 4
    # depth_player_2 = 1

    # depth_player_1 = 1
    # depth_player_2 = 4

    player_1 = player_agent_heuristics(heuristic_alpha_beta_tictacfive.alphabeta_max_h, heuristics.base_heuristic,
                                       depth_player_1)
    player_2 = player_agent_heuristics(heuristic_alpha_beta_tictacfive.alphabeta_min_h, heuristics.base_heuristic,
                                       depth_player_2)
    game_state.set_winning_length(5)
    grid = np.zeros((6, 6), dtype=int)
    grid[0, 1] = 1
    grid[1, 2] = 2
    init_state = game_state(grid, 1, (1, 2), 2)
    time_start = time.time()
    play_tictacfive(player_1, player_2, init_state)
    end_time = time.time() - time_start
    print(end_time)


def play_with_advanced_heuristics():
    depth_player_1 = 3
    depth_player_2 = 3
    # Does player 1 wins most of the games you play?
    player_1 = player_agent_heuristics(heuristic_alpha_beta_tictacfive.alphabeta_max_h, heuristics.advanced_heuristic,
                                       depth_player_1)
    player_2 = player_agent_heuristics(heuristic_alpha_beta_tictacfive.alphabeta_min_h, heuristics.base_heuristic,
                                       depth_player_2)
    game_state.set_winning_length(5)
    grid = np.zeros((10, 10), dtype=int)
    grid[5, 5] = 1
    grid[5, 4] = 2
    init_state = game_state(grid, 1, (5, 4), 2)
    time_start = time.time()
    play_tictacfive(player_1, player_2, init_state)
    end_time = time.time() - time_start
    print(end_time)



if __name__ == '__main__':
    #play_with_minimax()
    #play_with_alpha_beta()
    #play_with_heuristics()
    play_with_advanced_heuristics()
