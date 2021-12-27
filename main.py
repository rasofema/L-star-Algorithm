from classes.data_structure import Data_Structure
from classes.equivalence_oracle import Equivalence_Oracle
from classes.dfa import DFA

def algorithm(equivalence_oracle : Equivalence_Oracle, data_structure : Data_Structure) -> DFA:
    while True:
        hypothesis = data_structure.create_dfa()
        hypothesis_result = equivalence_oracle.accepts(hypothesis)
        if hypothesis_result == True:
            return hypothesis
        data_structure.add_counterexample(hypothesis_result)
