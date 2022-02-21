import random
from automata.dfa import DFA
from oracles.cache_oracle import Cache_Oracle
from oracles.oracle import Oracle

class Equivalence_Oracle(Oracle):
    def __init__(self, membership_oracle : Cache_Oracle):
        self.membership_oracle = membership_oracle
        self.counter = 0
    
    def accepts(self, hypothesis : DFA):
        alphabet = list(self.membership_oracle.get_alphabet())
        for _ in range(5000):
            self.counter += 1
            test_string = "".join(random.choices(alphabet, k=random.randint(1, 1000)))
            if hypothesis.accepts(test_string) != self.membership_oracle.accepts(test_string):
                return test_string
        return True
