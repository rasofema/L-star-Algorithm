from itertools import product
from classes.dfa import DFA
from classes.membership_oracle import Membership_Oracle

class Equivalence_Oracle():
    def __init__(self, membership_oracle : Membership_Oracle):
        self.membership_oracle = membership_oracle
    
    def accepts(self, hypothesis : DFA):
        alphabet = list(self.membership_oracle.dfa.alphabet)
        for size in range(1000):
            for test_string in [''.join(a) for a in product(alphabet, repeat=size)]:
                if hypothesis.accepts(test_string) != self.membership_oracle.accepts(test_string):
                    return test_string
        return True