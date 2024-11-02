import pennylane as qml
from pennylane import numpy as np

dev = qml.device("lightning.qubit", wires=3)

@qml.qnode(dev)
def mps_circuit():
    qml.BasisState(np.array([0, 0, 0]), wires=[0, 1, 2])

    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])

    m = qml.measure(wires=0)

    qml.cond(m, qml.PauliX)(wires=1)

    m2 = qml.measure(wires=1)

    qml.cond(m2, qml.PauliX)(wires=2)

    return qml.expval(qml.PauliZ(2))  


final_state = mps_circuit()
print("Estado final:", final_state)
