from abc import abstractmethod

from oracles.membership_oracle import Membership_Oracle


class Data_Structure():
    def __init__(self, alphabet : set, membership_oracle : Membership_Oracle):
        self.alphabet = alphabet
        self.membership_oracle = membership_oracle

    @abstractmethod
    def create_automata(self):
        raise NotImplementedError
    
    @abstractmethod
    def add_counterexample(self, counterexample):
        raise NotImplementedError