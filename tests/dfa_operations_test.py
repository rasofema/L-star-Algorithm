import dfa_operations

def dfa_union_same_alphabet(dfa1, dfa2):
    union = dfa_operations.union(dfa1, dfa2)
    assert union.accepts("") == True
    assert union.accepts("0") == False
    assert union.accepts("00") == True
    assert union.accepts("000") == True
    assert union.accepts("0000") == True
    assert union.accepts("00000") == False

def dfa_union_different_alphabet(dfa1, dfa3):
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

def dfa_complement(dfa1):
    complement = dfa_operations.complement(dfa1)
    assert complement.accepts("") == False
    assert complement.accepts("0") == True
    assert complement.accepts("00") == True
    assert complement.accepts("000") == False
    assert complement.accepts("0000") == True
    assert complement.accepts("00000") == True
    assert complement.accepts("000000") == False

def main(dfa1, dfa2, dfa3):
    dfa_union_same_alphabet(dfa1, dfa2)
    dfa_union_different_alphabet(dfa1, dfa3)
    dfa_complement(dfa1)
    return "dfa_operations_test: Everything passed"