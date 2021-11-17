class DFA():
    def __init__(self, states, alphabet, transitions, start_state, accepting_states):
        self.states = states                      #set
        self.alphabet = alphabet                  #set
        self.transitions = transitions            #dict of dict
        self.start_state = start_state
        self.accepting_states = accepting_states  #set

    def accepts(self, string):
        return self.reaching_state(string) in self.accepting_states
    
    def reaching_state(self, string):
        current_state = self.start_state

        for char in string:
            if char not in self.transitions[current_state]: #transition does not exist
                return None
            current_state = self.transitions[current_state][char]
        
        return current_state
