from abc import abstractmethod

from classes.equivalence_oracle import Equivalence_Oracle
from classes.membership_oracle import Membership_Oracle


class Data_Structure():
    def __init__(self, alphabet : set, membership_oracle : Membership_Oracle):
        self.alphabet = alphabet
        self.membership_oracle = membership_oracle

    @abstractmethod
    def create_dfa(self):
        raise NotImplementedError
    
    @abstractmethod
    def add_counterexample(self, counterexample):
        raise NotImplementedError