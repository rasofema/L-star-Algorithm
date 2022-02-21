from automata.dfa import DFA
from oracles.oracle import Oracle

class Membership_Oracle(Oracle):
    def __init__(self, dfa : DFA):
        self.dfa = dfa
    
    def accepts(self, string : str):
        return self.dfa.accepts(string)
