from automata.mealy_machine import Mealy_Machine


def mealy_machine_outputs(mealy_machine : Mealy_Machine):
    assert mealy_machine.final_output("") == None
    assert mealy_machine.final_output("0") == 0
    assert mealy_machine.final_output("00") == 0
    assert mealy_machine.final_output("000") == 1
    assert mealy_machine.final_output("0000") == 0

def mealy_machine_reaches_state(mealy_machine : Mealy_Machine):
    assert mealy_machine.reaching_state("") == 0
    assert mealy_machine.reaching_state("0") == 1
    assert mealy_machine.reaching_state("00") == 2
    assert mealy_machine.reaching_state("000") == 0
    assert mealy_machine.reaching_state("0000") == 1

def main(mealy_machine : Mealy_Machine):
    mealy_machine_outputs(mealy_machine)
    mealy_machine_reaches_state(mealy_machine)
    return "mealy_machine_test: Everything passed"
