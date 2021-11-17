import random

class oracle():
    def __init__(self, dfa):
        self.dfa = dfa
    
    def is_member(self, string):
        return self.dfa.accepts(string)
    
    def hypothesis_is_correct(self, hypothesis):
        alphabet = list(self.dfa.alphabet)
        for _ in range(1000):
            test_string = random.choices(alphabet, k=random.randint(0, 1000))
            if hypothesis.accepts(test_string) != self.dfa.accepts(test_string):
                return test_string
        return True