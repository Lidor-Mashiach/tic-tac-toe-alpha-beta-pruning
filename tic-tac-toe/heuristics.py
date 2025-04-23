def base_heuristic(curr_state):
    ## Note that...
    ## In this function, we will search for sequences of 3 and 4 with Forward Check
    ## in Addition, we will use Backward Check to find edges (empty nodes, "0")

    ## Initialize counters for Max and Min Players
    first_player_sequences_3 = 0
    first_player_sequences_4 = 0
    second_player_sequences_3 = 0
    second_player_sequences_4 = 0

    ## Map_State - current Map Grid
    map_state = curr_state.get_grid()
    ## Map Dimension, Using numpy shape method
    row_dimension, col_dimension = map_state.shape
    ## Directions to check: Horizontal, Vertical, Two Diagonals
    moves_to_check = [
        (0, 1),  ## Left - Right
        (1, 0),  ## Upper - Lower
        (1, 1),  ## Diagonal - From Upper Left to Lower Right
        (1, -1)  ## Diagonal - From Lower Left to Upper Right
    ]

    ## Scanning After Sequences all over the Grid(Map)
    for row in range(row_dimension):
        for col in range(col_dimension):
            ## Searching for unEmpty nodes
            if map_state[row, col] == 0:
                continue
            curr_player = map_state[row, col]

            ## we found an unEmpty Node - Now we need check the sequence for each move in moves_to_check
            for row_move, col_move in moves_to_check:
                sequence_length = 1
                ## Potential empty edges are the last Node and one node before the curr_player node.
                ## these Nodes will called "empty" if they contain the zero value - means 0
                empty_edges_counter = 0

                ## Forward check - Check from the potential position forward in the current direction
                for distance in range(1, 5):
                    next_row = row + row_move * distance
                    next_col = col + col_move * distance
                    valid_next_move = (0 <= next_row and next_row < row_dimension) and (0 <= next_col and next_col < col_dimension)

                    ## Check if the position is within the bounds of the board
                    if valid_next_move:
                        ## If same player as the original (original is curr_player)
                        if map_state[next_row, next_col] == curr_player:
                            sequence_length += 1

                        ## If empty cell (potential edge to count)
                        elif map_state[next_row, next_col] == 0:
                            empty_edges_counter += 1
                            break

                        ## Different player - the Sequence has broken
                        else:
                            break
                    # Out Of Boundary - the Sequence has broken
                    else:
                        break

                ## Check backward for additional edges
                back_row = row - row_move
                back_col = col - col_move
                valid_back_move = (0 <= back_row and back_row < row_dimension) and (0 <= back_col and back_col < col_dimension)
                ## Check if the backwards position is within the bounds of the board
                if valid_back_move:
                    if (map_state[back_row, back_col] == 0):
                        empty_edges_counter += 1
                ## Count sequences based on length and open ends
                if curr_player == 1:
                    if sequence_length == 4 and empty_edges_counter >= 1:
                        first_player_sequences_4 += 1
                    elif sequence_length == 3 and empty_edges_counter == 2:
                        first_player_sequences_3 += 1
                else:
                    if sequence_length == 4 and empty_edges_counter >= 1:
                        second_player_sequences_4 += 1
                    elif sequence_length == 3 and empty_edges_counter == 2:
                        second_player_sequences_3 += 1

    ## Calculate final heuristic value
    first_player_heuristic = first_player_sequences_3 + first_player_sequences_4
    second_player_heuristic = second_player_sequences_3 + second_player_sequences_4

    return first_player_heuristic - second_player_heuristic

def advanced_heuristic(curr_state):
    ## Note that...
    ## In this function, we will search for sequences of 3 and 4 with Forward Check
    ## in Addition, we will use Backward Check to find edges (empty nodes, "0")

    ## Initialize counters for Max and Min Players
    first_player_sequences_3 = 0
    first_player_sequences_4 = 0
    second_player_sequences_3 = 0
    second_player_sequences_4 = 0
    first_player_sequences_3_2_move_to_win = 0
    second_player_sequences_3_2_move_to_win = 0
    first_player_sequences_2_sure_win=0
    second_player_sequences_2_sure_win=0
    first_player_sequences_1_sure_win = 0
    second_player_sequences_1_sure_win = 0

    ## It should be noted that there are sequences of length 3 that lead to a sure win,
    ## and therefore they should be given the same importance as sequences of 4.
    ## for example:
    ## 2011102 - not sure winning, the enemy player can block us, and that's a regular 3 sequence
    ## 2101112  - sure winning for player 1 . And not taken into account at all in the Base heuristic function
    ## 200111012 - sure winning for player 1, not a regular 3 sequence. the next move should be 201111012 and from here its easy win for player 1
    first_player_sequences_3_sure_win = 0
    second_player_sequences_3_sure_win = 0

    ## There may be sequences of length 3 that are not currently a sure win, but could become one, so we want to detect them and give them a light weight in the heuristic calculation.
    ## It is important to note that if a sequence of length 3 is considered as sequences_3_sure_win it will not also count as an almost_winning sequence.
    ##for example :
    ## 2001112 - not sure winning, but can be
    first_player_almost_winning = 0
    second_player_almost_winning = 0
    ## Sequences in the middle of the map are strategic sequences that we want to give weight to, they open up the option for a wide variety of sequences.
    ## Every sequence in the middle will get an 1.5 more relevant


    ## Map_State - current Map Grid
    map_state = curr_state.get_grid()
    ## Map Dimension, Using numpy shape method
    row_dimension, col_dimension = map_state.shape
    ## Directions to check: Horizontal, Vertical, Two Diagonals
    moves_to_check = [
        (0, 1),  ## Left - Right
        (1, 0),  ## Upper - Lower
        (1, 1),  ## Diagonal - From Upper Left to Lower Right
        (1, -1)  ## Diagonal - From Lower Left to Upper Right
    ]

    ## Calculations for the sub-map that is the center of the large map
    center_row_start = row_dimension // 4
    center_row_end = row_dimension * 3 // 4
    center_col_start = col_dimension // 4
    center_col_end = col_dimension * 3 // 4

    potential_moves = curr_state.potential_moves()

    ## Scanning After Sequences all over the Grid(Map)
    for row, col in potential_moves:

            ## we found an unEmpty Node - Now we need check the sequence for each move in moves_to_check
            for row_move, col_move in moves_to_check:

                sequence_length = 0
                ## Potential empty edges are the last Node and one node before the curr_player node.
                ## these Nodes will called "empty" if they contain the zero value - means 0
                empty_edges_counter = 1
                ## garbage value
                curr_player = 3

                ## Forward check - Check from the potential position forward in the current direction
                for distance in range(1, 5):
                    next_row = row + row_move * distance
                    next_col = col + col_move * distance
                    ## next move boundary valid check
                    next_valid = (0 <= next_row and next_row < row_dimension) and (0 <= next_col and next_col < col_dimension)
                    ## Check if the position is within the bounds of the board
                    if next_valid:
                        if (distance == 1):
                            if (map_state[next_row, next_col] == 0):
                                curr_player = map_state[next_row, next_col]
                            else:
                                break
                        ## If same player as the original (original is curr_player)
                        if map_state[next_row, next_col] == curr_player:
                            sequence_length += 1

                        ## If empty cell (potential edge to count)
                        elif map_state[next_row, next_col] == 0:
                            empty_edges_counter += 1
                            break

                        ## Different player - the Sequence has broken
                        else:
                            break
                    ## Out Of Boundary - the Sequence has broken
                    else:
                        break

                ## Check backward for additional edges
                back_row = row - row_move
                back_col = col - col_move
                ## backward move boundary valid check
                back_valid = (0 <= back_row and back_row < row_dimension) and (0 <= back_col and back_col < col_dimension)


                ## A Boolean test that aims to check whether the sequence passes through the middle of the map
                is_in_center = (center_row_start <= row and row < center_row_end) and (center_col_start <= col and col < center_col_end)

                if sequence_length == 4:
                    if empty_edges_counter >= 1:
                        if curr_player == 1:
                            first_player_sequences_4 += 1
                            if is_in_center:
                                first_player_sequences_4 += 0.5
                        else:
                            second_player_sequences_4 += 1
                            if is_in_center:
                                second_player_sequences_4 += 0.5

                elif sequence_length == 3:
                    next_next_row = row + row_move * 4
                    next_next_col = col + col_move * 4
                    ## next-next move boundary valid check
                    next_next_valid = (0 <= next_next_row and next_next_row < row_dimension) and (0 <= next_next_col and next_next_col < col_dimension)
                    ## First thing - any sequence of length 3 with one open end will be defined as almost_winning
                    if empty_edges_counter == 1:
                        if curr_player == 1:
                            first_player_almost_winning += 1
                        else:
                            second_player_almost_winning += 1

                    if empty_edges_counter == 1:
                            ## check after sure winning 3 sequences like 2101112
                            if back_valid:
                                if map_state[back_row, back_col] == curr_player:
                                    if curr_player == 1:
                                        #We found that this is a sequence of length 3 that leads to a sure win.
                                        # Therefore, we will update sure_win accordingly, and decrement almost_winning by one to avoid double counting.
                                        first_player_sequences_3_sure_win += 1
                                        first_player_almost_winning-=1
                                        if is_in_center:
                                            first_player_sequences_3_sure_win += 0.5
                                    else:
                                        # We found that this is a sequence of length 3 that leads to a sure win.
                                        # Therefore, we will update sure_win accordingly, and decrement almost_winning by one to avoid double counting.
                                        second_player_sequences_3_sure_win += 1
                                        second_player_almost_winning -=1
                                        if is_in_center:
                                            second_player_sequences_3_sure_win += 0.5
                                    break
                    elif (empty_edges_counter == 2):
                        next_next_empty_edges_counter = 0
                        back_empty_edges_counter = 0
                        if back_valid:
                            ## searching after sure winning 3 sequences like 200111022
                            if (map_state[back_row, back_col] == 0):
                                back_empty_edges_counter += 1
                        if next_next_valid:
                            ## searching after sure winning 3 sequences like 220111002
                            if (map_state[next_next_row, next_next_col] == 0):
                                next_next_empty_edges_counter += 1

                        if (empty_edges_counter + next_next_empty_edges_counter) >= 1:
                            ## sure winning - 2 moves ahead
                            if curr_player == 1:
                                first_player_sequences_3_2_move_to_win += 1
                                first_player_almost_winning -= 1
                                if is_in_center:
                                    first_player_sequences_3_2_move_to_win += 0.5
                                break
                            else:
                                second_player_sequences_3_2_move_to_win += 1
                                second_player_almost_winning -= 1
                                if is_in_center:
                                    second_player_sequences_3_2_move_to_win += 0.5
                                break
                        else:
                            if curr_player == 1:
                                first_player_sequences_3 += 1
                                first_player_almost_winning -= 1
                                break
                            else:
                                second_player_sequences_3 += 1
                                second_player_almost_winning -= 1
                                break
                elif(sequence_length == 2):
                    ##searching after sure win sequences like 2110112
                    back_row = row - row_move
                    back_col = col - col_move
                    back_back_row = row - row_move*2
                    back_back_col = col - col_move*2
                    ## backward move boundary valid check
                    back_back_valid = (0 <= back_back_row and back_back_row < row_dimension) and (0 <= back_back_col and back_back_col < col_dimension)
                    if back_back_valid:
                        if map_state[back_row,back_col] == curr_player and map_state[back_back_row,back_back_col] == curr_player:
                            if curr_player == 1:
                                first_player_sequences_2_sure_win += 1
                                break
                            else:
                                second_player_sequences_2_sure_win += 1
                                break
                elif(sequence_length == 1):
                    ## searching after sure win sequences like 2111012
                    back_row = row - row_move
                    back_col = col - col_move
                    back_back_row = row - row_move * 2
                    back_back_col = col - col_move * 2
                    back_back_back_row = row - row_move*3
                    back_back_back_col = col - col_move*3
                    back_back_back_valid = (0 <= back_back_back_row and back_back_back_row < row_dimension) and (0 <= back_back_back_col and back_back_back_col < col_dimension)
                    if back_back_back_valid:
                        if map_state[back_row, back_col] == curr_player and map_state[back_back_row, back_back_col] == curr_player and map_state[back_back_back_row, back_back_back_col] == curr_player:
                            if curr_player == 1:
                                first_player_sequences_1_sure_win += 1
                                break
                            else:
                                second_player_sequences_1_sure_win += 1
                                break

    ## Calculate final heuristic value
    first_player_heuristic = (
            first_player_sequences_3 * 10 +
            first_player_sequences_4 * 1000 +
            first_player_sequences_3_sure_win * 1000 +
            first_player_sequences_2_sure_win * 1000 +
            first_player_sequences_1_sure_win * 1000 +
            first_player_almost_winning * 25 +
            first_player_sequences_3_2_move_to_win * 50
    )
    second_player_heuristic = (
            second_player_sequences_3 * 10 +
            second_player_sequences_4 * 1000 +
            second_player_sequences_3_sure_win * 1000 +
            second_player_sequences_2_sure_win * 1000 +
            second_player_sequences_1_sure_win * 1000 +
            second_player_almost_winning * 25 +
            second_player_sequences_3_2_move_to_win * 25
    )

    return first_player_heuristic - second_player_heuristic

















