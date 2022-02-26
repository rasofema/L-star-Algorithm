from oracles.membership_oracle import Membership_Oracle
from oracles.oracle import Oracle

class Cache_Oracle(Oracle):
    def __init__(self, oracle : Membership_Oracle):
        self.oracle = oracle
        self.cache = dict()
        self.counter = 0 # COUNTER
    
    def query(self, input):
        self.counter += 1
        if input in self.cache:
            return self.cache[input]
        result = self.oracle.query(input)
        self.cache[input] = result
        return result
    
    def get_alphabet(self):
        return self.oracle.get_alphabet()
