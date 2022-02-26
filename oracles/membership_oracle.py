from automata.automaton import Automaton
from oracles.oracle import Oracle

class Membership_Oracle(Oracle):
    def __init__(self, automaton : Automaton):
        self.automaton = automaton
    
    def query(self, string : str):
        return self.automaton.query(string)

    def get_alphabet(self):
        return self.automaton.alphabet