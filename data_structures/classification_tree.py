from data_structures.data_structure import Data_Structure
from automata.dfa import DFA
from oracles.membership_oracle import Membership_Oracle
from data_structures.data_structure import Data_Structure

class Node():
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
    
    def is_leaf(self):
        return self.left == None and self.right == None


class Classification_Tree(Data_Structure):
    def __init__(self, alphabet : set, membership_oracle : Membership_Oracle):
        super().__init__(alphabet, membership_oracle)
        self.root_node = Node("", None)

        if membership_oracle.query(""):
            self.root_node.right = Node("", self.root_node)
            self.root_node.left = None
        else:
            self.root_node.right = None
            self.root_node.left = Node("", self.root_node)

    
    def create_automata(self):
        access_strings = self.__get_access_strings(self.root_node)
        accepting_strings = self.__get_access_strings(self.root_node.right)

        transitions = dict()

        for s in access_strings:
            for a in self.alphabet:
                sift_result = self.__sift(s + a)
                if sift_result != None:
                    sift_result = sift_result.value
                
                if s not in transitions:
                    transitions[s] = {a : sift_result}
                else:
                    transitions[s][a] = sift_result
        
        return DFA(access_strings, self.alphabet, transitions, "", accepting_strings)


    def __get_access_strings(self, node):
        access_strings = set()

        if node != None:
            if node.is_leaf():
                access_strings.add(node.value)
            else:
                if node.left != None:
                    access_strings.update(self.__get_access_strings(node.left))
                if node.right != None:
                    access_strings.update(self.__get_access_strings(node.right))
        
        return access_strings


    def add_counterexample(self, counterexample):
        hypothesis = self.create_automata()

        prefix_size = 1
        sift_result = self.__sift(counterexample[:prefix_size])
        reaching_state = hypothesis.reaching_state(counterexample[:prefix_size])

        while prefix_size < len(counterexample):

            if sift_result == None: # from initialization
                if self.root_node.right == None:
                    self.root_node.right = Node(counterexample[:prefix_size], self.root_node)
                else:
                    self.root_node.left = Node(counterexample[:prefix_size], self.root_node)
                return
            
            if sift_result.value != reaching_state:
                break
            prefix_size += 1
            sift_result = self.__sift(counterexample[:prefix_size])
            reaching_state = hypothesis.reaching_state(counterexample[:prefix_size])

        node = self.__sift(counterexample[:prefix_size-1]) # the access string of prefix - 1
        prev_node = node.parent
        lca = self.__lowest_common_ancestor(self.root_node, sift_result.value, reaching_state)
        inner_node_value = counterexample[prefix_size-1] + lca.value
        old_node_value = node.value

        #substitute access string of prefix - 1 by new inner node
        if self.membership_oracle.query(old_node_value):
            prev_node.right = Node(inner_node_value, prev_node)
            node = prev_node.right
        else:
            prev_node.left = Node(inner_node_value, prev_node)
            node = prev_node.left

        # add leaves
        if self.membership_oracle.query(old_node_value + inner_node_value):
            node.right = Node(old_node_value, node)
            node.left = Node(counterexample[:prefix_size-1], node)
        else:
            node.right = Node(counterexample[:prefix_size-1], node)
            node.left = Node(old_node_value, node)


    def __sift(self, string) -> Node:
        current_node = self.root_node

        while True:
            if self.membership_oracle.query(string+current_node.value):
                current_node = current_node.right
            else:
                current_node = current_node.left
            
            if current_node == None or current_node.is_leaf():
                return current_node

    def __lowest_common_ancestor(self, node : Node, value1, value2):
        if node is None:
            return None
        
        if node.is_leaf() and (node.value == value1 or node.value == value2):
            return node
        
        left_subtree = self.__lowest_common_ancestor(node.left, value1, value2)
        right_subtree = self.__lowest_common_ancestor(node.right, value1, value2)

        if left_subtree is not None and right_subtree is not None:
            return node
        elif left_subtree is not None:
            return left_subtree
        else:
            return right_subtree
