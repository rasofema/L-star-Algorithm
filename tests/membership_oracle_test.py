def membership_query(oracle):
    assert oracle.accepts("") == True
    assert oracle.accepts("0") == False
    assert oracle.accepts("00") == False
    assert oracle.accepts("000") == True
    assert oracle.accepts("0000") == False

def main(oracle):
    membership_query(oracle)
    return "membership_oracle_test: Everything passed"