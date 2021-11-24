def hypothes_is_correct_query(oracle, dfa1, dfa2):
    assert oracle.hypothesis_is_correct(dfa1) == True
    assert oracle.hypothesis_is_correct(dfa2) != True

def main(oracle, dfa1, dfa2):
    hypothes_is_correct_query(oracle, dfa1, dfa2)
    return "equivalence_oracle_test: Everything passed"