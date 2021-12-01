from membership_oracle import Membership_Oracle
from equivalence_oracle import Equivalence_Oracle
from observation_table import Observation_Table
from dfa import DFA


# TODO: can the alphabet contain epsilon? There might be bugs in that case cause you can't append None to a string

def create_observation_table(alphabet, membership_oracle):
    epsilon_membership = membership_oracle.accepts("")

    prefixes_with_alphabet_membership = dict()
    for a in alphabet:
        prefixes_with_alphabet_membership[a] = membership_oracle.accepts(a)
    
    return Observation_Table(alphabet, epsilon_membership, prefixes_with_alphabet_membership)


def consistent(observation_table):
    prefixes = list(observation_table.prefixes_table.keys())
    for i in range(len(prefixes) - 1):
        for j in range(i + 1, len(prefixes)):
            prefix1 = prefixes[i]
            prefix2 = prefixes[j]
            if observation_table.prefixes_table[prefix1] == observation_table.prefixes_table[prefix2]:
                for a in observation_table.alphabet:
                    table = observation_table.prefixes_table | observation_table.prefixes_with_alphabet_table
                    if prefix1 == None:
                        prefix1 = ""
                    if prefix2 == None:
                        prefix2 = ""
                    if table[prefix1+a] != table[prefix2+a]:
                        return (prefix1, prefix2, a)
    return None 


def closed(observation_table):
    prefix_rows = observation_table.prefixes_table.values()

    for string, row in observation_table.prefixes_with_alphabet_table.items():
        if row not in prefix_rows:
            return string
    return None


def make_closed(observation_table, membership_oracle, cl):
    # move string from S.A to S
    observation_table.prefixes_table[cl] = observation_table.prefixes_with_alphabet_table[cl]
    del observation_table.prefixes_with_alphabet_table[cl]

    # expand S.A
    for a in observation_table.alphabet:
        string = cl+a
        table = observation_table.prefixes_table | observation_table.prefixes_with_alphabet_table
        if string not in table:
            string_with_suffixes_membership_list = []
            for suffix in observation_table.suffixes:
                if suffix == None:
                    suffix = ""
                string_with_suffixes_membership_list.append(membership_oracle.accepts(string+suffix))
            observation_table.prefixes_with_alphabet_table[string] = string_with_suffixes_membership_list


def make_consistent(observation_table, membership_oracle, prefix1, prefix2, suffix_a):
    table = observation_table.prefixes_table | observation_table.prefixes_with_alphabet_table
    row1 = table[prefix1+suffix_a]
    row2 = table[prefix2+suffix_a]

    for i in range(len(row1)):
        if row1[i] != row2[i]:
            # expand E
            suffix_e = observation_table.suffixes[i]
            if suffix_e == None:
                suffix_e = ""
            full_suffix = suffix_a + suffix_e
            observation_table.suffixes.append(full_suffix)

            # add membership queries to table
            for prefix in observation_table.prefixes_table:
                key = prefix
                if prefix == None:
                    prefix = ""
                observation_table.prefixes_table[key].append(membership_oracle.accepts(prefix+full_suffix))
            for prefix in observation_table.prefixes_with_alphabet_table:
                observation_table.prefixes_with_alphabet_table[prefix].append(membership_oracle.accepts(prefix+full_suffix))
            break


def make_table_closed_and_consistent(observation_table, membership_oracle):
    co = consistent(observation_table)
    cl = closed(observation_table)

    while co != None or cl != None:
        if co != None:
            prefix1 = co[0]
            prefix2 = co[1]
            suffix_a = co[2]
            make_consistent(observation_table, membership_oracle, prefix1, prefix2, suffix_a)
        
        if cl != None:
            make_closed(observation_table, membership_oracle, cl)
        
        co = consistent(observation_table)
        cl = closed(observation_table)


def create_dfa(observation_table):
    unique_rows_of_prefixes = [observation_table.prefixes_table[None]]
    for row in observation_table.prefixes_table.values():
        if row not in unique_rows_of_prefixes:
            unique_rows_of_prefixes.append(row)
    
    states = [_ for _ in range(len(unique_rows_of_prefixes))]

    alphabet = observation_table.alphabet

    transitions = dict()
    table = observation_table.prefixes_table | observation_table.prefixes_with_alphabet_table
    # for each state
    for i in range(len(unique_rows_of_prefixes)):
        state_row1 = unique_rows_of_prefixes[i]
        # find prefix string of that row
        for string, row in observation_table.prefixes_table.items():
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


def add_counterexample_to_table(counterexample, observation_table, membership_oracle):
    substrings = [str(counterexample[:i]) for i in range(len(counterexample), 0, -1)]
    # add substrings to S
    for substring in substrings:
        # check if substring not already in S
        if substring not in observation_table.prefixes_table:
            # substring in S.A
            if substring in observation_table.prefixes_with_alphabet_table:
                observation_table.prefixes_table[substring] = observation_table.prefixes_with_alphabet_table[substring]
                del observation_table.prefixes_with_alphabet_table[substring]
            else:
                substring_with_suffixes_membership_list = []
                for suffix in observation_table.suffixes:
                    if suffix == None:
                        suffix = ""
                    substring_with_suffixes_membership_list.append(membership_oracle.accepts(substring+suffix))
                observation_table.prefixes_table[substring] = substring_with_suffixes_membership_list
        
            # expand S.A
            for a in observation_table.alphabet:
                string = substring+a
                table = observation_table.prefixes_table | observation_table.prefixes_with_alphabet_table
                if string not in table:
                    string_with_suffixes_membership_list = []
                    for suffix in observation_table.suffixes:
                        if suffix == None:
                            suffix = ""
                        string_with_suffixes_membership_list.append(membership_oracle.accepts(string+suffix))
                    observation_table.prefixes_with_alphabet_table[string] = string_with_suffixes_membership_list


def main(target_dfa):
    alphabet = target_dfa.alphabet
    membership_oracle = Membership_Oracle(target_dfa)
    equivalence_oracle = Equivalence_Oracle(membership_oracle)

    observation_table = create_observation_table(alphabet, membership_oracle)

    while True:
        make_table_closed_and_consistent(observation_table, membership_oracle)
        hypothesis = create_dfa(observation_table)
        hypothesis_result = equivalence_oracle.accepts(hypothesis)
        if hypothesis_result == True:
            return hypothesis
        add_counterexample_to_table(hypothesis_result, observation_table, membership_oracle)
