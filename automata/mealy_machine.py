class Mealy_Machine():
    def __init__(self, states : set, start_state, input_alphabet : set, output_alphabet : set, transitions : dict, outputs : dict):
        self.states = states
        self.states.add(None)
        
        self.start_state = start_state
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.outputs = outputs

    def final_output(self, string : str):
        if len(string) == 0:
            return None
        penultimate_state = self.reaching_state(string[:-1])
        return self.outputs[penultimate_state][string[-1]]
        
    
    def reaching_state(self, string : str): # TODO: does it need to be public?
        current_state = self.start_state

        for char in string:
            if char not in self.transitions[current_state]: #transition does not exist
                return None
            current_state = self.transitions[current_state][char]
        
        return current_state
