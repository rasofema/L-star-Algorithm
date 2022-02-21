from time import sleep
from oracles.oracle import Oracle

class Cache_Oracle(Oracle):
    def __init__(self, oracle : Oracle):
        self.oracle = oracle
        self.cache = dict()
        self.counter = 0 # COUNTER
    
    def accepts(self, input):
        self.counter += 1
        if input in self.cache:
            return self.cache[input]
        result = self.oracle.accepts(input)
        self.cache[input] = result
        return result
    
    def get_alphabet(self):
        return self.oracle.dfa.alphabet
