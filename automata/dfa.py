from automata.automaton import Automaton

class DFA(Automaton):
    def __init__(self, states : set, alphabet : set, transitions : dict, start_state, accepting_states : set):
        super().__init__(states, start_state, alphabet, transitions)
        self.accepting_states = accepting_states

    def query(self, string : str):
        return self.reaching_state(string) in self.accepting_states
    
    def reaching_state(self, string : str):
        current_state = self.start_state

        for char in string:
            if current_state == None or char not in self.transitions[current_state]: #transition does not exist
                return None
            current_state = self.transitions[current_state][char]
        
        return current_state
    
    def is_empty(self):
        visited = set()
        queue = [self.start_state]

        while(queue):
            state = queue.pop(0)
            visited.add(state)
            for reachable_state in self.transitions[state].values():
                if reachable_state not in visited:
                    queue.append(reachable_state)
        
        for state in visited:
            if state in self.accepting_states:
                return False
        
        return True
