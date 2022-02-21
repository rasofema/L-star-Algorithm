from oracles.membership_oracle import Membership_Oracle


def membership_query(oracle : Membership_Oracle):
    assert oracle.accepts("") == True
    assert oracle.accepts("0") == False
    assert oracle.accepts("00") == False
    assert oracle.accepts("000") == True
    assert oracle.accepts("0000") == False

def main(oracle : Membership_Oracle):
    membership_query(oracle)
    return "membership_oracle_test: Everything passed"