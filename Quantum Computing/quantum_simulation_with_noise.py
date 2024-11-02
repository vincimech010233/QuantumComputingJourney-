from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer.noise import NoiseModel, depolarizing_error
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

noise_model = NoiseModel()
error_prob = 0.05  

error_1 = depolarizing_error(error_prob, 1)
error_2 = depolarizing_error(error_prob, 2)
noise_model.add_all_qubit_quantum_error(error_1, ['h'])
noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

simulator = AerSimulator(noise_model=noise_model)

qc_transpiled = transpile(qc, simulator)

job = simulator.run(qc_transpiled)

result = job.result()
counts = result.get_counts(qc_transpiled)

print("Resultados con ruido:", counts)

plot_histogram(counts)
plt.show()
