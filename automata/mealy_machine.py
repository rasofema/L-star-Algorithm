from automata.automaton import Automaton

class Mealy_Machine(Automaton):
    def __init__(self, states : set, start_state, input_alphabet : set, output_alphabet : set, transitions : dict, outputs : dict):
        super().__init__(states, start_state, input_alphabet, transitions)
        self.output_alphabet = output_alphabet
        self.outputs = outputs

    def query(self, string : str):
        if len(string) == 0:
            return None
        penultimate_state = self.reaching_state(string[:-1])
        return self.outputs[penultimate_state][string[-1]]
        
    
    def reaching_state(self, string : str):
        current_state = self.start_state

        for char in string:
            if char not in self.transitions[current_state]: #transition does not exist
                return None
            current_state = self.transitions[current_state][char]
        
        return current_state
