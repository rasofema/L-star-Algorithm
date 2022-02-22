from time import perf_counter
from automata.dfa_operations import complement, union
from data_structures.classification_tree import Classification_Tree
from data_structures.data_structure import Data_Structure
from automata.dfa_generator import DFA_Generator
from automata.dfa import DFA
from oracles.cache_oracle import Cache_Oracle

from oracles.equivalence_oracle import Equivalence_Oracle
from oracles.membership_oracle import Membership_Oracle
from data_structures.observation_table import Observation_Table
from main import algorithm

NUMBER_OF_STATES = [1, 10, 20, 50, 100, 200]

def get_running_time(dfa, data_structure : Data_Structure):
    membership_oracle = Cache_Oracle(Membership_Oracle(dfa))
    equivalence_oracle = Equivalence_Oracle(membership_oracle)

    start_time = perf_counter()
    algorithm(equivalence_oracle, data_structure(dfa.alphabet, membership_oracle))
    end_time = perf_counter()
    
    return (end_time - start_time, membership_oracle.counter - equivalence_oracle.counter)

def random_dfa():
    transitions = dict()
    transitions[0] = {'a' : 1, 'b' : 0}
    transitions[1] = {'a' : 1, 'b' : 2}
    transitions[2] = {'a' : 1, 'b' : 3}
    transitions[3] = {'a' : 1, 'b' : 0}
    return DFA({0, 1, 2, 3}, {'a', 'b'}, transitions, 0, {3})

if __name__ == "__main__":
    print("-----------START TESTING-----------")

    print("RANDOM DFA")
    result = get_running_time(random_dfa(), Observation_Table)
    print("TABLE - Time elapsed: " + str(result[0]))
    print(" - Number of membership queries: " + str(result[1]))
    result = get_running_time(random_dfa(), Classification_Tree)
    print("TREE - Time elapsed: " + str(result[0]))
    print(" - Number of membership queries: " + str(result[1]))

    print()
    print("OBSERVATION TABLE - ALPHABET SIZE: 1")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0'}), Observation_Table)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
    
    print("OBSERVATION TABLE - ALPHABET SIZE: 2")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0', '1'}), Observation_Table)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))

    print()
    print("CLASSIFICATION TREE - ALPHABET SIZE: 1")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0'}), Classification_Tree)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
    
    print("CLASSIFICATION TREE - ALPHABET SIZE: 2")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0', '1'}), Classification_Tree)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
    
    print("-------------ALL PASSED------------")
