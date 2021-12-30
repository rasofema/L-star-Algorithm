from classes.mealy_machine import Mealy_Machine

# outputs 1 on input with a length multiple of n, 0 for the rest
class Mealy_Machine_Generator(Mealy_Machine):
    def __init__(self, n : int, alphabet : set):
        states = set(range(n))
        start_state = 0

        transitions = dict()
        outputs = dict()
        for i in range(n-1):
            transitions[i] = dict()
            outputs[i] = dict()
            for char in alphabet:
                transitions[i][char] = i+1
                outputs[i][char] = 0


        transitions[n-1] = dict()
        outputs[n-1] = dict()
        for char in alphabet:
            transitions[n-1][char] = 0
            outputs[n-1][char] = 1

        super().__init__(states, start_state, alphabet, {0, 1}, transitions, outputs)