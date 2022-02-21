from math import e
from typing import Tuple
from data_structures.data_structure import Data_Structure
from automata.dfa import DFA
from oracles.membership_oracle import Membership_Oracle
from data_structures.data_structure import Data_Structure

class Observation_Table(Data_Structure):
    def __init__(self, alphabet : set, membership_oracle : Membership_Oracle):
        super().__init__(alphabet, membership_oracle)
        self.suffixes = [None]                                              # E
        self.prefixes_table = {None : [membership_oracle.accepts("")]}      # S
        self.prefixes_with_alphabet_table = dict()                          # S·A

        for a in alphabet:
            self.prefixes_with_alphabet_table[a] = [membership_oracle.accepts(a)]
    
    def create_dfa(self) -> DFA:
        self.__make_closed_and_consistent()

        unique_rows_of_prefixes = [self.prefixes_table[None]]
        for row in self.prefixes_table.values():
            if row not in unique_rows_of_prefixes:
                unique_rows_of_prefixes.append(row)
        
        states = set([_ for _ in range(len(unique_rows_of_prefixes))])

        alphabet = self.alphabet

        transitions = dict()
        table = self.prefixes_table | self.prefixes_with_alphabet_table
        # for each state
        for i in range(len(unique_rows_of_prefixes)):
            state_row1 = unique_rows_of_prefixes[i]
            # find prefix string of that row
            for string, row in self.prefixes_table.items():
                if row == state_row1:
                    # add transition for each alphabet element
                    for a in alphabet:
                        # find state of string+a
                        if string == None:
                            string = ""
                        row_string_plus_a = table[string+a]
                        for j in range(len(unique_rows_of_prefixes)):
                            if row_string_plus_a == unique_rows_of_prefixes[j]:
                                # add transition
                                if i in transitions:
                                    transitions[i][a] = j
                                else:
                                    transitions[i] = {a : j}
                                break
                    break

        start_state = 0

        accepting_states = set()
        for i in range(len(unique_rows_of_prefixes)):
            if unique_rows_of_prefixes[i][0] == True:
                accepting_states.add(i)

        return DFA(states, alphabet, transitions, start_state, accepting_states)


    def __make_closed_and_consistent(self):
        co : Tuple(str, str, chr) = self.__consistent()
        cl : str = self.__closed()

        while co != None or cl != None:
            if co != None:
                prefix1 : str = co[0]
                prefix2 : str = co[1]
                suffix_a : chr = co[2]
                self.__make_consistent(prefix1, prefix2, suffix_a)
            
            if cl != None:
                self.__make_closed(cl)
            
            co = self.__consistent()
            cl = self.__closed()

    def __consistent(self):
        prefixes = list(self.prefixes_table.keys())
        for i in range(len(prefixes) - 1):
            for j in range(i + 1, len(prefixes)):
                prefix1 : str = prefixes[i]
                prefix2 : str = prefixes[j]
                if self.prefixes_table[prefix1] == self.prefixes_table[prefix2]:
                    for a in self.alphabet:
                        table = self.prefixes_table | self.prefixes_with_alphabet_table
                        if prefix1 == None:
                            prefix1 = ""
                        if prefix2 == None:
                            prefix2 = ""
                        if table[prefix1+a] != table[prefix2+a]:
                            return (prefix1, prefix2, a)
        return None

    def __closed(self):
        prefix_rows = self.prefixes_table.values()

        for string, row in self.prefixes_with_alphabet_table.items():
            if row not in prefix_rows:
                return string
        return None

    def __make_consistent(self, prefix1, prefix2, suffix_a):
        table = self.prefixes_table | self.prefixes_with_alphabet_table
        row1 = table[prefix1+suffix_a]
        row2 = table[prefix2+suffix_a]

        for i in range(len(row1)):
            if row1[i] != row2[i]:
                # expand E
                suffix_e = self.suffixes[i]
                if suffix_e == None:
                    suffix_e = ""
                full_suffix = suffix_a + suffix_e
                self.suffixes.append(full_suffix)

                # add membership queries to table
                for prefix in self.prefixes_table:
                    key = prefix
                    if prefix == None:
                        prefix = ""
                    self.prefixes_table[key].append(self.membership_oracle.accepts(prefix+full_suffix))
                for prefix in self.prefixes_with_alphabet_table:
                    self.prefixes_with_alphabet_table[prefix].append(self.membership_oracle.accepts(prefix+full_suffix))
                break
    
    def __make_closed(self, cl):
        # move string from S.A to S
        self.prefixes_table[cl] = self.prefixes_with_alphabet_table[cl]
        del self.prefixes_with_alphabet_table[cl]

        # expand S.A
        for a in self.alphabet:
            string = cl+a
            table = self.prefixes_table | self.prefixes_with_alphabet_table
            if string not in table:
                string_with_suffixes_membership_list = []
                for suffix in self.suffixes:
                    if suffix == None:
                        suffix = ""
                    string_with_suffixes_membership_list.append(self.membership_oracle.accepts(string+suffix))
                self.prefixes_with_alphabet_table[string] = string_with_suffixes_membership_list

    def add_counterexample(self, counterexample):
        substrings = [str(counterexample[:i]) for i in range(len(counterexample), 0, -1)]
        # add substrings to S
        for substring in substrings:
            # check if substring not already in S
            if substring not in self.prefixes_table:
                # substring in S.A
                if substring in self.prefixes_with_alphabet_table:
                    self.prefixes_table[substring] = self.prefixes_with_alphabet_table[substring]
                    del self.prefixes_with_alphabet_table[substring]
                else:
                    substring_with_suffixes_membership_list = []
                    for suffix in self.suffixes:
                        if suffix == None:
                            suffix = ""
                        substring_with_suffixes_membership_list.append(self.membership_oracle.accepts(substring+suffix))
                    self.prefixes_table[substring] = substring_with_suffixes_membership_list
            
                # expand S.A
                for a in self.alphabet:
                    string = substring+a
                    table = self.prefixes_table | self.prefixes_with_alphabet_table
                    if string not in table:
                        string_with_suffixes_membership_list = []
                        for suffix in self.suffixes:
                            if suffix == None:
                                suffix = ""
                            string_with_suffixes_membership_list.append(self.membership_oracle.accepts(string+suffix))
                        self.prefixes_with_alphabet_table[string] = string_with_suffixes_membership_list
