from time import perf_counter
from classes.classification_tree import Classification_Tree
from classes.data_structure import Data_Structure
from classes.dfa_generator import DFA_Generator

from classes.equivalence_oracle import Equivalence_Oracle
from classes.membership_oracle import Membership_Oracle
from classes.observation_table import Observation_Table
from main import algorithm

NUMBER_OF_STATES = [1, 10, 20, 50, 100, 200]

def get_running_time(dfa, data_structure : Data_Structure):
    membership_oracle = Membership_Oracle(dfa)
    equivalence_oracle = Equivalence_Oracle(membership_oracle)

    start_time = perf_counter()
    algorithm(equivalence_oracle, data_structure(dfa.alphabet, membership_oracle, equivalence_oracle))
    end_time = perf_counter()

    return (end_time - start_time, membership_oracle.counter - equivalence_oracle.counter, membership_oracle.counter)


if __name__ == "__main__":
    print("-----------START TESTING-----------")
    """ print("OBSERVATION TABLE - ALPHABET SIZE: 1")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0'}), Observation_Table)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
        print(" - Number of membership queries including equivalence queries: " + str(result[2]))
    
    print("OBSERVATION TABLE - ALPHABET SIZE: 2")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0', '1'}), Observation_Table)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
        print(" - Number of membership queries including equivalence queries: " + str(result[2]))
 """
    print("CLASSIFICATION TREE - ALPHABET SIZE: 1")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0'}), Classification_Tree)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
        print(" - Number of membership queries including equivalence queries: " + str(result[2]))
    
    print("CLASSIFICATION TREE - ALPHABET SIZE: 2")
    for n in NUMBER_OF_STATES:
        result = get_running_time(DFA_Generator(n, {'0', '1'}), Classification_Tree)
        print("Number of states: " + str(n) + "; Time elapsed: " + str(result[0]))
        print(" - Number of membership queries: " + str(result[1]))
        print(" - Number of membership queries including equivalence queries: " + str(result[2]))

    print("-------------ALL PASSED------------")
