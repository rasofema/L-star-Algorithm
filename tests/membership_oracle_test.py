from automata.dfa import DFA
from automata.mealy_machine import Mealy_Machine
from oracles.membership_oracle import Membership_Oracle
from test import membership_oracle


def membership_query_dfa(dfa : DFA):
    oracle = membership_oracle(dfa)
    assert oracle.query("") == True
    assert oracle.query("0") == False
    assert oracle.query("00") == False
    assert oracle.query("000") == True
    assert oracle.query("0000") == False

def membership_query_mealy_machine(mealy_machine : Mealy_Machine):
    oracle = membership_oracle(mealy_machine)
    assert oracle.query("") == None
    assert oracle.query("0") == 0
    assert oracle.query("00") == 0
    assert oracle.query("000") == 1
    assert oracle.query("0000") == 0

def main(dfa : DFA, mealy_machine : Mealy_Machine):
    membership_query_dfa(dfa)
    membership_query_mealy_machine(mealy_machine)
    return "membership_oracle_test: Everything passed"