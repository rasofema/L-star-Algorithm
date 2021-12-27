from classes.dfa_operations import complement, union
from classes.equivalence_oracle import Equivalence_Oracle
from classes.membership_oracle import Membership_Oracle
from classes.classification_tree import Classification_Tree
from main import algorithm

def run(dfa):
    membership_oracle = Membership_Oracle(dfa)
    result = algorithm(Equivalence_Oracle(membership_oracle), Classification_Tree(dfa.alphabet, membership_oracle, Equivalence_Oracle(membership_oracle)))

    xor = complement(union(union(complement(result), dfa), union(complement(dfa), result)))
    assert xor.is_empty()

def main(dfa_list):
    for dfa in dfa_list:
        run(dfa)
    return "classification_tree_test: Everything passed"