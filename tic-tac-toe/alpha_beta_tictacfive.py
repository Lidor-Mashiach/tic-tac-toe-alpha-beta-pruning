import math


## Check if pruning is available for Max player (X).
def alphabeta_max(current_game):
    alpha_value = -math.inf
    beta_value = math.inf
    return maximin(current_game, alpha_value, beta_value)


## Check if pruning is available for Min player (○).
def alphabeta_min(current_game):
    alpha_value = -math.inf
    beta_value = math.inf
    return minimax(current_game, alpha_value, beta_value)



## Finds The Best Move For Max Player (X)
## Recursively evaluates all possible moves to maximize the score for Max.
## Uses alpha-beta pruning to optimize calculations.
def maximin(current_game, alpha_value, beta_value):
    if current_game.is_terminal():
        ## No more Moves Available - Current_Game is a leaf on Minimax Game Tree
        return current_game.get_score(), None
    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        ## Next Turn Is Min Player (○), So do the next calculations with MiniMax Func.
        mx, next_move = minimax(move, alpha_value, beta_value)
        if v < mx:
            v = mx
            best_move = move
        ## Check if pruning is needed for Max player (X).
        alpha_value = max(alpha_value, v)
        if (alpha_value >= beta_value):
        ## Pruning is available
            break
    return v, best_move



## Finds The Best Move For Min Player (○)
## Recursively evaluates all possible moves to maximize the score for Min.
## Uses alpha-beta pruning to optimize calculations
def minimax(current_game, alpha_value, beta_value):
    if current_game.is_terminal():
        ## No more Moves Available - Current_Game is a leaf on Minimax Game Tree
        return current_game.get_score(), None
    v = math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        ## Next Turn Is Max Player (X), So do the next calculations with Maximin Func.
        mx, next_move = maximin(move, alpha_value, beta_value)
        if v > mx:
            v = mx
            best_move = move
        beta_value = min(beta_value, v)
        if (alpha_value >= beta_value):
            ## Pruning is available
            break
    return v, best_move
