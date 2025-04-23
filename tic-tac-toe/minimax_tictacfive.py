import math


## Finds The Best Move For Max Player (X)
## Recursively evaluates all possible moves to maximize the score for Max.
def maximin(current_game):
    ## Current_Game is the current State of the Game Board
    if current_game.is_terminal():
        ## no more Moves Available - Current_game is a leaf on Minimax Game Tree
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        ## Next Turn Is Min Player (○), So do the next calculations with MiniMax Func.
        mx, next_move = minimax(move)
        if v < mx:
            v = mx
            best_move = move
    ## Best_Move Is the Best Move that Max Player Can Do
    ## V is the Value of Best_Move - The Maximal Value
    return v, best_move



    ## Finds The Best Move For Min Player (○)
    ## Recursively evaluates all possible moves to maximize the score for Min.
def minimax(current_game):
    ## Current_Game is the current State of the Game Board
    if current_game.is_terminal():
        ## no more Moves Available - Current_game is a leaf on Minimax Game Tree
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        ## Next Turn Is Max Player (X), So do the next calculations with Maximin Func.
        mx, next_move = maximin(move)
        if v > mx:
            v = mx
            best_move = move
    ## Best_Move Is the Best Move that Min Player Can Do
    ## V is the Value of Best_Move - The Minimal Value
    return v, best_move

