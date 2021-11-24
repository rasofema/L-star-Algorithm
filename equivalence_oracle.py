import random

from membership_oracle import Membership_Oracle

class Equivalence_Oracle():
    def __init__(self, dfa):
        self.membership_oracle = Membership_Oracle(dfa)
    
    def hypothesis_is_correct(self, hypothesis):
        alphabet = list(self.membership_oracle.dfa.alphabet)
        for _ in range(1000):
            test_string = random.choices(alphabet, k=random.randint(0, 1000))
            if hypothesis.accepts(test_string) != self.membership_oracle.accepts(test_string):
                return test_string
        return True