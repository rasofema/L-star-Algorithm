from automata import dfa_operations
from automata.dfa import DFA

def dfa_union_same_alphabet(dfa1 : DFA, dfa2 : DFA):
    union = dfa_operations.union(dfa1, dfa2)
    assert union.query("") == True
    assert union.query("0") == False
    assert union.query("00") == True
    assert union.query("000") == True
    assert union.query("0000") == True
    assert union.query("00000") == False

def dfa_union_different_alphabet(dfa1 : DFA, dfa3 : DFA):
    union = dfa_operations.union(dfa1, dfa3)
    assert union.query("") == True
    assert union.query("0") == False
    assert union.query("00") == False
    assert union.query("000") == True
    assert union.query("0000") == False
    assert union.query("00000") == False
    assert union.query("000000") == True
    assert union.query("11111") == False
    assert union.query("1111") == True
    assert union.query("111") == False
    assert union.query("11") == True
    assert union.query("1") == False

def dfa_complement(dfa1 : DFA):
    complement = dfa_operations.complement(dfa1)
    assert complement.query("") == False
    assert complement.query("0") == True
    assert complement.query("00") == True
    assert complement.query("000") == False
    assert complement.query("0000") == True
    assert complement.query("00000") == True
    assert complement.query("000000") == False

def main(dfa1 : DFA, dfa2 : DFA, dfa3 : DFA):
    dfa_union_same_alphabet(dfa1, dfa2)
    dfa_union_different_alphabet(dfa1, dfa3)
    dfa_complement(dfa1)
    return "dfa_operations_test: Everything passed"