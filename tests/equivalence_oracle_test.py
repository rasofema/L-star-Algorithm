def hypothes_is_correct_query(oracle, dfa1, dfa2):
    assert oracle.accepts(dfa1) == True
    assert oracle.accepts(dfa2) != True

def main(oracle, dfa1, dfa2):
    hypothes_is_correct_query(oracle, dfa1, dfa2)
    return "equivalence_oracle_test: Everything passed"