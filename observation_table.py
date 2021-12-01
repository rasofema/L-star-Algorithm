class Observation_Table():
    def __init__(self, alphabet, epsilon_membership, prefixes_with_alphabet_membership):
        self.alphabet = alphabet
        self.suffixes = [None] # E
        self.prefixes_table = dict() # S
        self.prefixes_with_alphabet_table = dict() # S·A

        self.prefixes_table[None] = [epsilon_membership]
        for key in prefixes_with_alphabet_membership:
            self.prefixes_with_alphabet_table[key] = [prefixes_with_alphabet_membership[key]]