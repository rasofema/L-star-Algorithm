from classes.dfa_generator import DFA_Generator
from classes.membership_oracle import Membership_Oracle
from classes.equivalence_oracle import Equivalence_Oracle
from tests import dfa_test, dfa_operations_test, membership_oracle_test, equivalence_oracle_test, observation_table_test, classification_tree_test


def membership_oracle(dfa):
    return Membership_Oracle(dfa)

def equivalence_oracle(dfa):
    return Equivalence_Oracle(membership_oracle(dfa))



if __name__ == "__main__":
    dfa1 = DFA_Generator(3, {'0'})
    dfa2 = DFA_Generator(2, {'0'})
    dfa3 = DFA_Generator(2, {'1'})

    print("-----------START TESTING-----------")
    print(dfa_test.main(dfa1))
    print(dfa_operations_test.main(dfa1, dfa2, dfa3))
    print(membership_oracle_test.main(membership_oracle(dfa1)))
    print(equivalence_oracle_test.main(equivalence_oracle(dfa1), dfa1, dfa2))
    print(observation_table_test.main([dfa1, dfa2, dfa3]))
    print(classification_tree_test.main([dfa1, dfa2, dfa3]))
    print("-------------ALL PASSED------------")
