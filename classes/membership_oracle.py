from classes.dfa import DFA

class Membership_Oracle():
    def __init__(self, dfa : DFA):
        self.dfa = dfa
        self.counter = 0 #COUNTER
    
    def accepts(self, string : str):
        self.counter += 1 #COUNTER
        return self.dfa.accepts(string)
