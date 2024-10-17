import math

"""
function MINIMAX-SEARCH(game, state) returns an action
  player←game.TO-MOVE(state)
  value, move←MAX-VALUE(game, state)
  return move

function MAX-VALUE(game, state) returns a (utility, move) pair
  if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null 
  v, move←−∞
  for each a in game.ACTIONS(state) do
    v2, a2←MIN-VALUE(game, game.RESULT(state, a)) 
    if v2 > v then
      v, move←v2, a 
  return v, move

function MIN-VALUE(game, state) returns a (utility, move) pair
  if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null 
  v, move←+∞
  for each a in game.ACTIONS(state) do
    v2, a2←MAX-VALUE(game, game.RESULT(state, a)) 
    if v2 < v then
      v, move←v2, a 
  return v, move
"""


def minimax_search(game, state):
    """
    Perform the minimax search algorithm to determine the best move for the current player.

    The minimax algorithm is a recursive method used in decision-making and game theory.
    It provides an optimal move for the player assuming that the opponent also plays optimally.
    The algorithm works by simulating all possible moves, evaluating the resulting game states,
    and choosing the move that maximizes the player's minimum gain (hence the name "minimax").

    Parameters:
    game (Game): An instance of the game being played. It should provide methods like `is_terminal`, `utility`, `actions`, `result`, and `to_move`.
    state (State): The current state of the game. This is typically a representation of the game board or configuration.

    Returns:
    Action | None: The best action for the current player to take. If no actions are available (e.g., in a terminal state), it returns None.
    """

    def min_value(game, state):
        """
        Compute the minimum utility value for the opponent's move.

        This function is called when it is the opponent's turn to move.
        It recursively evaluates all possible moves and returns the move that minimizes the utility value for the opponent.

        Parameters:
        game (Game): An instance of the game being played.
        state (State): The current state of the game.

        Returns:
        tuple[float, Action | None]: A tuple containing the minimum utility value and the corresponding action. If the state is terminal, it returns the utility value and None.
        """
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = math.inf, None
        for a in game.actions(state):
            v2, a2 = max_value(game, game.result(state, a))
            if v2 < v:
                v, move = v2, a
        return v, move

    def max_value(game, state):
        """
        Compute the maximum utility value for the current player's move.

        This function is called when it is the current player's turn to move.
        It recursively evaluates all possible moves and returns the move that maximizes the utility value for the current player.

        Parameters:
        game (Game): An instance of the game being played.
        state (State): The current state of the game.

        Returns:
        tuple[float, Action | None]: A tuple containing the maximum utility value and the corresponding action. If the state is terminal, it returns the utility value and None.
        """
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -math.inf, None
        for a in game.actions(state):
            v2, a2 = min_value(game, game.result(state, a))
            if v2 > v:
                v, move = v2, a
        return v, move

    # player is captured within the closure of the min_value and max_value functions
    # a cleaner approach would be to pass player as an argument or get player from the min and max functions
    # but we choose to follow the pseudocode from the book as closely as possible
    player = game.to_move(state)
    val, move = max_value(game, state)
    return move
