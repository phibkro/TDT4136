import math

"""
function ALPHA-BETA-SEARCH(game, state) returns an action 
    player←game.TO-MOVE(state)
    value, move←MAX-VALUE(game, state,−∞,+∞)
    return move

    function MAX-VALUE(game, state, α, β) returns a (utility, move) pair
        if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null 
        v←−∞
        for each a in game.ACTIONS(state) do
            v2, a2←MIN-VALUE(game, game.RESULT(state, a),α,β) 
            if v2 > v then
                v, move←v2, a
                α←MAX(α, v)
            if v ≥ β then return v, move
        return v, move

    function MIN-VALUE(game, state, α, β) returns a (utility, move) pair
        if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null 
            v←+∞
        for each a in game.ACTIONS(state) do
            v2, a2←MAX-VALUE(game, game.RESULT(state, a),α,β) 
            if v2 < v then
                v, move←v2, a
                β←MIN(β, v)
            if v ≤ α then return v, move
        return v, move
"""


def alpha_beta_search(game, state):
    """
    Perform the alpha-beta pruning algorithm to determine the best move for the current player.

    Alpha-beta pruning is an optimization technique for the minimax algorithm.
    It reduces the number of nodes evaluated in the search tree by pruning branches that cannot influence the final decision.
    This makes the search more efficient without affecting the result.

    Parameters:
    game (Game): An instance of the game being played. It should provide methods like `is_terminal`, `utility`, `actions`, `result`, and `to_move`.
    state (State): The current state of the game. This is typically a representation of the game board or configuration.

    Returns:
    Action | None: The best action for the current player to take. If no actions are available (e.g., in a terminal state), it returns None.
    """
    player = game.to_move(state)

    def max_value(game, state, alpha, beta):
        """
        Compute the maximum utility value for the current player's move using alpha-beta pruning.

        This function is called when it is the current player's turn to move.
        It recursively evaluates all possible moves and returns the move that maximizes the utility value for the current player,
        while pruning branches that cannot affect the final decision.

        Parameters:
        game (Game): An instance of the game being played.
        state (State): The current state of the game.
        alpha (float): The best value that the maximizer currently can guarantee at that level or above.
        beta (float): The best value that the minimizer currently can guarantee at that level or above.

        Returns:
        tuple[float, Action | None]: A tuple containing the maximum utility value and the corresponding action. If the state is terminal, it returns the utility value and None.
        """
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -math.inf, None
        for a in game.actions(state):
            v2, a2 = min_value(game, game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)  # Update alpha
            if v >= beta:
                return v, move  # Prune the search
        return v, move

    def min_value(game, state, alpha, beta):
        """
        Compute the minimum utility value for the opponent's move using alpha-beta pruning.

        This function is called when it is the opponent's turn to move.
        It recursively evaluates all possible moves and returns the move that minimizes the utility value for the opponent,
        while pruning branches that cannot affect the final decision.

        Parameters:
        game (Game): An instance of the game being played.
        state (State): The current state of the game.
        alpha (float): The best value that the maximizer currently can guarantee at that level or above.
        beta (float): The best value that the minimizer currently can guarantee at that level or above.

        Returns:
        tuple[float, Action | None]: A tuple containing the minimum utility value and the corresponding action. If the state is terminal, it returns the utility value and None.
        """
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = math.inf, None
        for a in game.actions(state):
            v2, a2 = max_value(game, game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)  # Update beta
            if v <= alpha:
                return v, move  # Prune the search
        return v, move

    val, move = max_value(game, state, -math.inf, math.inf)
    return move
