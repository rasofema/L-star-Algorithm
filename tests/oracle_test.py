def membership_query(oracle):
    assert oracle.is_member("") == True
    assert oracle.is_member("0") == False
    assert oracle.is_member("00") == False
    assert oracle.is_member("000") == True
    assert oracle.is_member("0000") == False

def hypothes_is_correct_query(oracle1, dfa1, dfa2):
    assert oracle1.hypothesis_is_correct(dfa1) == True
    assert oracle1.hypothesis_is_correct(dfa2) != True

def main(oracle1, dfa1, dfa2):
    membership_query(oracle1)
    hypothes_is_correct_query(oracle1, dfa1, dfa2)
    return "oracle_test: Everything passed"