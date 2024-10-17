def simulate(game, strategy):
    """Simulate a game using the given strategy.

    Parameters:
    game (Game): An instance of the game being played.
    strategy (function): A function that takes the game and the current state as input and returns the best action for the current player.
    """
    state = game.initial_state()
    game.print(state)
    while not game.is_terminal(state):
        player = game.to_move(state)
        action = strategy(game, state)
        print(f"P{player+1}'s action: {action}")
        assert action is not None
        state = game.result(state, action)
        game.print(state)


if __name__ == "__main__":
    from search.minimax import minimax_search
    from search.alpha_beta import alpha_beta_search
    from games.bucket_game import Game as BucketGame
    from games.halving_game import Game as HalvingGame
    from games.tictactoe import Game as TicTacToeGame

    if True:
        print("""a) Text outputs showing the actual playing of the different games with the Minimax
    algorithm for both players. The output should include the state of the game at every
    turn, the action performed and by whom, and who won the game at the end or if the
    game ended in a draw.""")

        print("Simulating bucket game with minimax search:")
        simulate(BucketGame(), minimax_search)
        print()

        print("Simulating halving game with minimax search:")
        simulate(HalvingGame(5), minimax_search)
        print()

        print("Simulating TicTacToe game with minimax search:")
        simulate(TicTacToeGame(), minimax_search)

    if True:
        print("""b) The runtime of finding the first move for Tic-tac-toe with Minimax compared to
    alpha-beta pruning.""")
        print()
        from time import time

        start = time()
        action = minimax_search(TicTacToeGame(), TicTacToeGame().initial_state())
        end = time()

        print(f"Time taken for Minimax: {end - start:.2f} seconds")

        start = time()
        action = alpha_beta_search(TicTacToeGame(), TicTacToeGame().initial_state())
        end = time()

        print(f"Time taken for Alpha-Beta Pruning: {end - start:.2f} seconds")
