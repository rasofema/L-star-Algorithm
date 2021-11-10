from DFA import DFA

states = {0, 1, 2}
alphabet = {0}
transitions = {
    0: {'0' : 1},
    1: {'0' : 2},
    2: {'0' : 0},
    }
start_state = 0
accepting_states = {0}

dfa = DFA(states, alphabet, transitions, start_state, accepting_states)


def dfa_accepts_string():
    assert dfa.accepts("") == True
    assert dfa.accepts("0") == False
    assert dfa.accepts("00") == False
    assert dfa.accepts("000") == True
    assert dfa.accepts("0000") == False

def dfa_reaches_state():
    assert dfa.reaching_state("") == 0
    assert dfa.reaching_state("0") == 1
    assert dfa.reaching_state("00") == 2
    assert dfa.reaching_state("000") == 0
    assert dfa.reaching_state("0000") == 1


if __name__ == "__main__":
    dfa_accepts_string()
    dfa_reaches_state()
    print("Everything passed")
