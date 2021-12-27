from classes.dfa import DFA

# accepts strings with a length multiple of n
class DFA_Generator(DFA):
    def __init__(self, n : int, alphabet : set):
        states = set(range(n))
        transitions = dict()
        for i in range(n-1):
            transitions[i] = dict()
            for char in alphabet:
                transitions[i][char] = i+1
        
        transitions[n-1] = dict()
        for char in alphabet:
            transitions[n-1][char] = 0

        start_state = 0
        accepting_states = {0}
        super().__init__(states, alphabet, transitions, start_state, accepting_states)