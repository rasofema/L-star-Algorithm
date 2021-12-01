from itertools import product

class Equivalence_Oracle():
    def __init__(self, membership_oracle):
        self.membership_oracle = membership_oracle
    
    def accepts(self, hypothesis):
        alphabet = list(self.membership_oracle.dfa.alphabet)
        for size in range(1000):
            for test_string in [''.join(a) for a in product(alphabet, repeat=size)]:
                if hypothesis.accepts(test_string) != self.membership_oracle.accepts(test_string):
                    return test_string
        return True