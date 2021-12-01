from classes.dfa import DFA

class Membership_Oracle():
    def __init__(self, dfa : DFA):
        self.dfa = dfa
    
    def accepts(self, string : str):
        return self.dfa.accepts(string)
