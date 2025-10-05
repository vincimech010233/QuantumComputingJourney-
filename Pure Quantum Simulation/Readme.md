# 🔬 Computación Cuántica desde Cero

> Algoritmos cuánticos implementados solo con NumPy y SciPy - Sin Pennylane ni Qiskit

## 🎯 ¿Qué es esto?

Cuadernos de Google Colab que implementan algoritmos cuánticos usando únicamente álgebra lineal. Aprende computación cuántica viendo cada operación matricial, sin cajas negras.

## 📚 Algoritmos

- **QAOA** - Minimum Vertex Cover, MaxCut
- **VQE** *(próximamente)*
- **Grover** *(próximamente)*

## 🛠️ Dependencias

Solo necesitas: `numpy`, `scipy`, `matplotlib`

**No requiere**: Pennylane, Qiskit, Cirq ni hardware cuántico

## 🚀 Uso
```python
edges = [[0, 1], [1, 2], [0, 2]]
qaoa = QAOAPurePython(edges)
optimal_params = qaoa.optimize(p_layers=2)
