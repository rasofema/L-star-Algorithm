def dfa_accepts_string(dfa1):
    assert dfa1.accepts("") == True
    assert dfa1.accepts("0") == False
    assert dfa1.accepts("00") == False
    assert dfa1.accepts("000") == True
    assert dfa1.accepts("0000") == False

def dfa_reaches_state(dfa1):
    assert dfa1.reaching_state("") == 0
    assert dfa1.reaching_state("0") == 1
    assert dfa1.reaching_state("00") == 2
    assert dfa1.reaching_state("000") == 0
    assert dfa1.reaching_state("0000") == 1

def main(dfa1):
    dfa_accepts_string(dfa1)
    dfa_reaches_state(dfa1)
    return "dfa_test: Everything passed"
