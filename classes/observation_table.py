from classes.membership_oracle import Membership_Oracle

class Observation_Table():
    def __init__(self, alphabet : set, membership_oracle : Membership_Oracle):
        self.alphabet = alphabet
        self.suffixes = [None]                                              # E
        self.prefixes_table = {None : [membership_oracle.accepts("")]}      # S
        self.prefixes_with_alphabet_table = dict()                          # S·A

        for a in alphabet:
            self.prefixes_with_alphabet_table[a] = [membership_oracle.accepts(a)]
    
