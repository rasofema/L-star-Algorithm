from abc import abstractmethod


class Automaton():
    def __init__(self, states : set, start_state, alphabet : set, transitions : dict):
        self.states = states
        self.states.add(None)

        self.start_state = start_state
        self.transitions = transitions
        self.alphabet = alphabet

    @abstractmethod
    def query(self, string : str):
        raise NotImplementedError
    
    @abstractmethod
    def reaching_state(self, string : str):
        raise NotImplementedError
