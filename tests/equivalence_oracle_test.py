from automata.dfa import DFA
from oracles.equivalence_oracle import Equivalence_Oracle


def hypothes_is_correct_query(oracle : Equivalence_Oracle, dfa1 : DFA, dfa2 : DFA):
    assert oracle.accepts(dfa1) == True
    assert oracle.accepts(dfa2) != True

def main(oracle : Equivalence_Oracle, dfa1 : DFA, dfa2 : DFA):
    hypothes_is_correct_query(oracle, dfa1, dfa2)
    return "equivalence_oracle_test: Everything passed"