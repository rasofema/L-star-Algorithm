from dfa import DFA
from oracle import oracle
from tests import dfa_test, dfa_operations_test, oracle_test

def dfa1(): # DFA 1 - accepts strings with a number of 0s multiple of 3
    states = {0, 1, 2, None}
    alphabet = {'0'}
    transitions = {
        0: {'0' : 1},
        1: {'0' : 2},
        2: {'0' : 0},
        }
    start_state = 0
    accepting_states = {0}

    return DFA(states, alphabet, transitions, start_state, accepting_states)

def dfa2(): # DFA 2 - accepts strings with a number of 0s multiple of 2
    states = {0, 1, None}
    alphabet = {'0'}
    transitions = {
        0: {'0' : 1},
        1: {'0' : 0}
        }
    start_state = 0
    accepting_states = {0}

    return DFA(states, alphabet, transitions, start_state, accepting_states)

def dfa3(): # DFA 3 - accepts strings with a number of 1s multiple of 2
    states = {0, 1, None}
    alphabet = {'1'}
    transitions = {
        0: {'1' : 1},
        1: {'1' : 0}
        }
    start_state = 0
    accepting_states = {0}

    return DFA(states, alphabet, transitions, start_state, accepting_states)

def oracle1():
    return oracle(dfa1())

if __name__ == "__main__":
    print(dfa_test.main(dfa1()))
    print(dfa_operations_test.main(dfa1(), dfa2(), dfa3()))
    print(oracle_test.main(oracle1(), dfa1(), dfa2()))