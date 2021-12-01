class DFA():
    def __init__(self, states : set, alphabet : set, transitions : dict, start_state, accepting_states : set):
        self.states = states
        self.states.add(None)
        
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    def accepts(self, string : str):
        return self.reaching_state(string) in self.accepting_states
    
    def reaching_state(self, string : str):
        current_state = self.start_state

        for char in string:
            if char not in self.transitions[current_state]: #transition does not exist
                return None
            current_state = self.transitions[current_state][char]
        
        return current_state
