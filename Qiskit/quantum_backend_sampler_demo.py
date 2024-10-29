from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.primitives import Sampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Usar el servicio de IBM Quantum
service = QiskitRuntimeService()
backend = service.backend('ibmq_qasm_simulator')  # Cambia a un backend real si tienes acceso

sampler = Sampler(backend=backend)
job = sampler.run(qc)
result = job.result()
print("Resultados del Sampler con IBM Quantum:", result)

simulator = Aer.get_backend('aer_simulator')
sampler = Sampler(backend=simulator)
job = sampler.run(qc)
result = job.result()
print("Resultados del Sampler con Aer:", result)
