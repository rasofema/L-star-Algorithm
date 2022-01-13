from typing import Tuple
from classes.data_structure import Data_Structure
from classes.dfa import DFA
from classes.membership_oracle import Membership_Oracle
from classes.equivalence_oracle import Equivalence_Oracle
from classes.data_structure import Data_Structure

class Node():
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
    
    def is_leaf(self):
        return self.left == None and self.right == None

class Classification_Tree(Data_Structure):
    def __init__(self, alphabet : set, membership_oracle : Membership_Oracle, equivalence_oracle : Equivalence_Oracle):
        super().__init__(alphabet, membership_oracle)
        self.root_node = Node("", None)

        transitions = {0 : dict()}
        for a in alphabet:
            transitions[0][a] = 0

        accepting_states = set()
        if membership_oracle.accepts(""):
            accepting_states.add(0)

        result = equivalence_oracle.accepts(DFA({0}, alphabet, transitions, 0, accepting_states))
        
        if accepting_states:
            self.root_node.right = Node("", self.root_node)
        else:
            self.root_node.left = Node("", self.root_node)

        if result != True:
            if accepting_states:
                self.root_node.left = Node(result, self.root_node)
            else:
                self.root_node.right = Node(result, self.root_node)

    
    def create_dfa(self):
        access_strings = set()
        self.__get_access_strings(access_strings, self.root_node)

        accepting_strings = set()
        if self.root_node.right != None:
            self.__get_access_strings(accepting_strings, self.root_node.right)

        transitions = dict()

        for s in access_strings:
            for a in self.alphabet:
                sift_result = self.__sift(s + a).value
                if s not in transitions:
                    transitions[s] = {a : sift_result}
                else:
                    transitions[s][a] = sift_result
        
        return DFA(access_strings, self.alphabet, transitions, "", accepting_strings)


    def __get_access_strings(self, lst, node):
        if node.is_leaf():
            lst.add(node.value)
        else:
            if node.left != None:
                self.__get_access_strings(lst, node.left)
            if node.right != None:
                self.__get_access_strings(lst, node.right)


    def add_counterexample(self, counterexample):
        hypothesis = self.create_dfa()

        prefix_size = 1
        while prefix_size < len(counterexample):
            sift_result = self.__sift(counterexample[:prefix_size])
            reaching_state = hypothesis.reaching_state(counterexample[:prefix_size])
            if sift_result.value != reaching_state:
                break
            prefix_size += 1
        
        prev_node = sift_result.parent
        if self.membership_oracle.accepts(counterexample[:prefix_size-1]+prev_node.value):
            value = prev_node.right.value
            prev_node.right = Node(counterexample[prefix_size-1] + prev_node.value, prev_node)
            prev_node.right.right = Node(value, prev_node.right)
            prev_node.right.left = Node(counterexample[:prefix_size-1], prev_node.right)
        else:
            value = prev_node.left.value
            prev_node.left = Node(counterexample[prefix_size-1] + prev_node.value, prev_node)
            prev_node.left.left = Node(value, prev_node.left)
            prev_node.left.right = Node(counterexample[:prefix_size-1], prev_node.left)


    def __sift(self, string) -> Node:
        current_node = self.root_node

        while True:
            if self.membership_oracle.accepts(string+current_node.value):
                current_node = current_node.right
            else:
                current_node = current_node.left
            
            if current_node.is_leaf():
                return current_node
