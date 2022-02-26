from automata.dfa import DFA


def dfa_accepts_string(dfa : DFA):
    assert dfa.query("") == True
    assert dfa.query("0") == False
    assert dfa.query("00") == False
    assert dfa.query("000") == True
    assert dfa.query("0000") == False

def dfa_reaches_state(dfa : DFA):
    assert dfa.reaching_state("") == 0
    assert dfa.reaching_state("0") == 1
    assert dfa.reaching_state("00") == 2
    assert dfa.reaching_state("000") == 0
    assert dfa.reaching_state("0000") == 1

def main(dfa : DFA):
    dfa_accepts_string(dfa)
    dfa_reaches_state(dfa)
    return "dfa_test: Everything passed"
