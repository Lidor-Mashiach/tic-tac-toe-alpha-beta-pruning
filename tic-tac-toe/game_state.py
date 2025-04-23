"""
game_state represents the game board, players location on the board and the current player to play a move.
"""


class game_state:
    winning_length = 5

    def __init__(self, grid, curr_player, last_move, used_cells):
        """
        :param grid: matrix that represents the grid during this turn
        :param curr_player: the player that its turn currently
        :param last_move: last move played by the previous player
        :param used_cells: cells that are used by either player
        """
        self.__grid = grid
        self.__curr_player = curr_player
        self.__last_move = last_move
        self.__used_cells = used_cells
        self.__score = -1

    @classmethod
    def set_winning_length(cls, length):
        cls.winning_length = length

    def get_used_cells(self):
        return self.__used_cells

    def get_grid(self):
        return self.__grid

    def get_curr_player(self):
        return self.__curr_player

    def get_last_move(self):
        return self.__last_move

    def set_curr_player(self, curr_player):
        self.__curr_player = curr_player

    def potential_moves(self):
        """
        :return: set of all legal moves for the current player
        """
        rows, cols = self.__grid.shape

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        moves = set()

        for x in range(rows):
            for y in range(cols):
                if self.__grid[x, y] != 0:
                    # Check adjacent cells
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        # Check if the neighbor is within bounds and is zero
                        if 0 <= nx < rows and 0 <= ny < cols and self.__grid[nx, ny] == 0:
                            moves.add((nx, ny))  #
        return moves

    def get_moves(self):
        """
        :return: All possible game_state objects after performing a legal move during this turn
        for each new game_state, we switch the current player to the other player.
        """
        moves = self.potential_moves()
        new_games = []
        next_player = 1 if self.__curr_player == 2 else 2

        for move in moves:
            cpy_grid = self.__grid.copy()
            cpy_grid[move] = self.__curr_player
            new_games.append(game_state(cpy_grid, next_player, move, self.__used_cells + 1))

        return new_games

    def is_legal_location(self, curr_location):
        """
        :param curr_location: the location we want to check
        :return: True if curr_location is a legal location for current player to move to, False otherwise
        """
        if (curr_location[0] < 0 or curr_location[0] >= len(self.__grid)
                or curr_location[1] < 0 or curr_location[1] >= len(self.__grid[1])):
            return False
        return self.__grid[curr_location] == 0

    def is_terminal(self):
        """
        :return: True if there are no legal moves for the current player or a winning position achieved
                    and False otherwise
        """
        rows, cols = self.__grid.shape
        if self.__used_cells == rows * cols:
            self.__score = 0
            return True
        if self.has_consecutive():
            self.__score = 1000 if self.__curr_player == 2 else -1000
            # prolong the game
            # self.__score -= self.__used_cells
            return True
        return False

    def has_consecutive(self):
        rows, cols = self.__grid.shape

        directions = [
            (0, 1),
            (1, 0),
            (1, 1),
            (1, -1)
        ]
        other_player = 1 if self.__curr_player == 2 else 2

        for x in range(rows):
            for y in range(cols):
                if self.__grid[x, y] == other_player:
                    for dx, dy in directions:
                        count = 1
                        for i in range(1, game_state.winning_length):
                            nx, ny = x + i * dx, y + i * dy
                            # Check if the next position is within bounds and matches the value
                            if 0 <= nx < rows and 0 <= ny < cols and self.__grid[nx, ny] == self.__grid[x, y]:
                                count += 1
                            else:
                                break
                        if count == game_state.winning_length:
                            return True
        return False

    def apply_move(self, move):
        """
        :param move: to be applied by the current player
        move the current player and switch the turn to the opposing player.
        """
        self.__grid[move] = self.__curr_player
        self.__last_move = move
        self.__curr_player = (self.__curr_player % 2) + 1
        self.__used_cells += 1

    def get_score(self):
        """
        :return: the current score of the game.
        value = 1000 points is just an arbitrary high number, you can change its value.
        This value is large enough so that the heuristic value will be between 1000 and -1000.
        """
        return self.__score
