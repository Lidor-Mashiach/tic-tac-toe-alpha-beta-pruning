# 🎮 Game AI – Minimax and Alpha-Beta Pruning on Extended Tic-Tac-Toe

This project implements an intelligent AI agent for a generalized version of **Tic-Tac-Toe** (also known as "Five in a Row" or **TicTacFive**), where the game is played on larger boards with configurable win conditions.

Using **Minimax search** and **Alpha-Beta pruning**, the system explores the game tree to make optimal decisions for each player.  
In addition, the project supports **depth-limited search with heuristic evaluation**, allowing scalable play on large boards such as 6×6 or 10×10.

The framework is modular, supporting:
- ✅ Standard Minimax and Alpha-Beta pruning
- 🚀 Heuristic-based pruning for faster AI in large grids
- 🎯 Pluggable heuristics for strategic evaluation
- 🧪 Easy testing of AI matchups with configurable depth

Developed in an academic context to demonstrate **game tree search**, **adversarial reasoning**, and **pruning optimization**.

---
## 📁 Project Structure & Key Components

- `game_engine.py`  
  Core logic for running the game loop.  
  - Handles turn alternation, board state updates, and win/tie detection.
  - Supports dynamic board sizes and custom win-length settings.

- `game_state.py`  
  Models the game board and legal moves.  
  - Represents the current state of the board.
  - Provides valid actions and handles deep copies for state simulation.

- `player_agent.py`  
  Interface for AI and human agents.  
  - Allows switching between algorithmic players and manual input.
  - Supports hybrid play for debugging and comparison.

- `minimax_tictacfive.py`  
  Implements the classic **Minimax algorithm**.  
  - Recursively explores all possible future game states.
  - Chooses the move that maximizes the player's chance to win.

- `alpha_beta_tictacfive.py`  
  Optimized version using **Alpha-Beta pruning**.  
  - Reduces the number of evaluated nodes by pruning irrelevant branches.
  - Maintains correctness while significantly improving performance.

- `heuristic_alpha_beta_tictacfive.py`  
  A depth-limited version of Alpha-Beta with **heuristic evaluation**.  
  - Supports large boards by limiting recursion depth.
  - Uses domain-specific heuristics to evaluate non-terminal states.

- `heuristics.py`  
  Contains multiple heuristic functions:
  - Line scoring based on potential win sequences.
  - Threat detection and blocking opportunities.

Each component is decoupled and well-documented, allowing independent testing, improvement, and experimentation.

---

## 🧠 How It Works – AI Decision-Making

This project explores the construction of an intelligent AI agent for an extended Tic-Tac-Toe game (e.g., 5-in-a-row on large boards).  
The focus is on evaluating decision-making depth, efficiency, and effectiveness across different algorithms.

1. **Game Setup**
   - Players take turns placing markers (`X` or `O`) on a dynamic-sized board.
   - A player wins by forming a consecutive line (row, column, or diagonal) of predefined length (e.g., 5).
   - The engine supports both human and AI players.

2. **AI Algorithms**
   - **Minimax**:  
     - Explores the entire game tree recursively.
     - Guarantees optimal moves but becomes slow on large boards due to exponential growth.
   - **Alpha-Beta Pruning**:  
     - Improves Minimax by cutting off branches that cannot affect the outcome.
     - Drastically reduces the number of states evaluated while preserving optimality.
   - **Heuristic Alpha-Beta**:  
     - Introduces a depth limit to the search.
     - Uses custom heuristics to evaluate board states when the depth is reached.
     - Enables fast and reasonable decisions even on 10x10 or 15x15 boards.

3. **Heuristics**
   - The AI evaluates partially completed lines, potential threats, and blocking opportunities.
   - Assigns scores based on the number of contiguous pieces, open ends, and interruption by the opponent.
   - Supports scalable play with reasonable runtime on large boards.

4. **Performance Comparison**
   - You can toggle between algorithms to observe:
     - Move decision time
     - Aggressiveness vs. defensiveness
     - Accuracy of moves based on board state complexity


---

## ▶️ How to Run

> 🧪 This project was developed for academic and practical exploration of game AI.  
> You can run it from the command line and experiment with different board sizes and AI strategies.

1. Make sure all project files are in the same directory:
   - `game_engine.py`
   - `game_state.py`
   - `player_agent.py`
   - `minimax_tictacfive.py`
   - `alpha_beta_tictacfive.py`
   - `heuristic_alpha_beta_tictacfive.py`
   - `heuristics.py`

2. Run the game:
```bash
  python game_engine.py
```

3. You’ll be prompted to configure:
   - **Board size** (e.g., `10x10`, `15x15`)
   - **Winning sequence length** (e.g., `5`)
   - **Player types**:
     - Human vs AI
     - AI vs Human
     - AI vs AI
   - **AI strategy** (for each AI player):
     - Minimax
     - Alpha-Beta Pruning
     - Heuristic Alpha-Beta Pruning


The game runs in the console and displays the updated board after each move.

🧠 Feel free to explore, tweak the heuristics, or challenge the AI with your own strategy!
