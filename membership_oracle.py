import random

class Membership_Oracle():
    def __init__(self, dfa):
        self.dfa = dfa
    
    def accepts(self, string):
        return self.dfa.accepts(string)
