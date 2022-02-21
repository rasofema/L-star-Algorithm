from automata.dfa import DFA
from automata.dfa_operations import complement, union
from oracles.cache_oracle import Cache_Oracle
from oracles.equivalence_oracle import Equivalence_Oracle
from oracles.membership_oracle import Membership_Oracle
from data_structures.classification_tree import Classification_Tree
from main import algorithm

def run(dfa : DFA):
    membership_oracle = Cache_Oracle(Membership_Oracle(dfa))
    equivalence_oracle = Equivalence_Oracle(membership_oracle)
    result = algorithm(equivalence_oracle, Classification_Tree(dfa.alphabet, membership_oracle))

    xor = complement(union(union(complement(result), dfa), union(complement(dfa), result)))
    assert xor.is_empty()

def main(dfa_list : list):
    for dfa in dfa_list:
        run(dfa)
    return "classification_tree_test: Everything passed"