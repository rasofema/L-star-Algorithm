from DFA import DFA
import dfa_operations

# DFA 1 - accepts strings with a number of 0s multiple of 3
states = {0, 1, 2, None}
alphabet = {'0'}
transitions = {
    0: {'0' : 1},
    1: {'0' : 2},
    2: {'0' : 0},
    }
start_state = 0
accepting_states = {0}

dfa1 = DFA(states, alphabet, transitions, start_state, accepting_states)

# DFA 2 - accepts strings with a number of 0s multiple of 2
states = {0, 1, None}
alphabet = {'0'}
transitions = {
    0: {'0' : 1},
    1: {'0' : 0}
    }
start_state = 0
accepting_states = {0}

dfa2 = DFA(states, alphabet, transitions, start_state, accepting_states)

# DFA 3 - accepts strings with a number of 1s multiple of 2
states = {0, 1, None}
alphabet = {'1'}
transitions = {
    0: {'1' : 1},
    1: {'1' : 0}
    }
start_state = 0
accepting_states = {0}

dfa3 = DFA(states, alphabet, transitions, start_state, accepting_states)


def dfa_accepts_string():
    assert dfa1.accepts("") == True
    assert dfa1.accepts("0") == False
    assert dfa1.accepts("00") == False
    assert dfa1.accepts("000") == True
    assert dfa1.accepts("0000") == False

def dfa_reaches_state():
    assert dfa1.reaching_state("") == 0
    assert dfa1.reaching_state("0") == 1
    assert dfa1.reaching_state("00") == 2
    assert dfa1.reaching_state("000") == 0
    assert dfa1.reaching_state("0000") == 1

def dfa_union_same_alphabet():
    union = dfa_operations.union(dfa1, dfa2)
    assert union.accepts("") == True
    assert union.accepts("0") == False
    assert union.accepts("00") == True
    assert union.accepts("000") == True
    assert union.accepts("0000") == True
    assert union.accepts("00000") == False

def dfa_union_different_alphabet():
    union = dfa_operations.union(dfa1, dfa3)
    assert union.accepts("") == True
    assert union.accepts("0") == False
    assert union.accepts("00") == False
    assert union.accepts("000") == True
    assert union.accepts("0000") == False
    assert union.accepts("00000") == False
    assert union.accepts("000000") == True
    assert union.accepts("11111") == False
    assert union.accepts("1111") == True
    assert union.accepts("111") == False
    assert union.accepts("11") == True
    assert union.accepts("1") == False

if __name__ == "__main__":
    dfa_accepts_string()
    dfa_reaches_state()
    dfa_union_same_alphabet()
    dfa_union_different_alphabet()
    print("Everything passed")
