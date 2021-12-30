from classes.dfa_operations import complement, union
from classes.equivalence_oracle import Equivalence_Oracle
from classes.membership_oracle import Membership_Oracle
from classes.observation_table import Observation_Table
from main import algorithm
from test import equivalence_oracle

def run(dfa):
    membership_oracle = Membership_Oracle(dfa)
    equivalence_oracle = Equivalence_Oracle(membership_oracle)
    result = algorithm(equivalence_oracle, Observation_Table(dfa.alphabet, membership_oracle, equivalence_oracle))

    xor = complement(union(union(complement(result), dfa), union(complement(dfa), result)))
    assert xor.is_empty()

def main(dfa_list):
    for dfa in dfa_list:
        run(dfa)
    return "observation_table_test: Everything passed"