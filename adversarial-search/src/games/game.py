from abc import ABC, abstractmethod


class Game(ABC):
    """Game
    A class representing a two-player, zero-sum game.
    The game is defined by the following methods:
    - initial_state(): Return the initial state of the game.
    - to_move(state): Return the player to move in the given state.
    - actions(state): Return a list of legal moves in the given state.
    - result(state, action): Return the resulting state after applying the given action to the given state.
    - is_terminal(state): Return True if the given state is terminal, False otherwise.
    - utility(state, player): Return the utility value of the given state for the given player.
    - print(state): Print the given state.
    """

    @abstractmethod
    def initial_state(self):
        raise NotImplementedError("initial_state() must be implemented")

    @abstractmethod
    def to_move(self):
        raise NotImplementedError("to_move() must be implemented")

    @abstractmethod
    def actions(self):
        raise NotImplementedError("actions() must be implemented")

    @abstractmethod
    def result(self):
        raise NotImplementedError("result() must be implemented")

    @abstractmethod
    def is_terminal(self):
        raise NotImplementedError("is_terminal() must be implemented")

    @abstractmethod
    def utility(self):
        raise NotImplementedError("utility() must be implemented")

    @abstractmethod
    def print(self):
        raise NotImplementedError("print() must be implemented")
