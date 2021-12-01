from main import algorithm

def run(dfa):
    result = algorithm(dfa)

    assert result.states == dfa.states
    assert result.alphabet == dfa.alphabet
    assert result.transitions == dfa.transitions
    assert result.start_state == dfa.start_state
    assert result.accepting_states == dfa.accepting_states

def main(dfa1, dfa2, dfa3):
    run(dfa1)
    run(dfa2)
    run(dfa3)
    return "main_test: Everything passed"