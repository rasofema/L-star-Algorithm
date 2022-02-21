import itertools
from automata.dfa import DFA

def union(dfa1 : DFA, dfa2 : DFA):
    states = set(itertools.product(dfa1.states, dfa2.states))
    alphabet = set.union(dfa1.alphabet, dfa2.alphabet)

    transitions = dict()
    for state in states:
        transitions[state] = dict()
        for char in alphabet:

            reach_state1 = None
            if state[0] != None and char in dfa1.transitions[state[0]]:
                reach_state1 = dfa1.transitions[state[0]][char]

            reach_state2 = None
            if state[1] != None and char in dfa2.transitions[state[1]]:
                reach_state2 = dfa2.transitions[state[1]][char]
            
            transitions[state][char] = (reach_state1, reach_state2)

    
    start_state = (dfa1.start_state, dfa2.start_state)
    accepting_states = set.union(
        set(itertools.product(dfa1.accepting_states, dfa2.states)),
        set(itertools.product(dfa1.states, dfa2.accepting_states))
        )
    
    return DFA(states, alphabet, transitions, start_state, accepting_states)

def complement(dfa):
    return DFA(dfa.states, dfa.alphabet, dfa.transitions, dfa.start_state, dfa.states.difference(dfa.accepting_states))