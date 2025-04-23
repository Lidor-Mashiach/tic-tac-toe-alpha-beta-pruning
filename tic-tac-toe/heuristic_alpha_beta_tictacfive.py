import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    alpha_value = -math.inf
    beta_value = math.inf
    return maximin(current_game, depth, alpha_value, beta_value)


def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    alpha_value = -math.inf
    beta_value = math.inf
    return minimax(current_game, depth, alpha_value, beta_value)


def maximin(current_game, depth, alpha_value, beta_value):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1, alpha_value, beta_value)
        if v < mx:
            v = mx
            best_move = move
        alpha_value = max(alpha_value, v)
        if (alpha_value >= beta_value):
            ## Pruning is available
            break
    return v, best_move


def minimax(current_game, depth, alpha_value, beta_value):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1, alpha_value, beta_value)
        if v > mx:
            v = mx
            best_move = move
        beta_value = min(beta_value, v)
        if (alpha_value >= beta_value):
            ## Pruning is available
            break
    return v, best_move
