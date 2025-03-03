from qiskit import QuantumCircuit, transpile, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

# Crear el circuito de Superdense Coding con 2 qubits y 2 bits clásicos
circuito = QuantumCircuit(2)

# Agregar un registro clásico con 2 bits para la medición
creg = ClassicalRegister(2, 'c')
circuito.add_register(creg)

# PASO 1: CREACIÓN DEL PAR ENTRELAZADO ENTRE ALICE Y BOB
circuito.h(0)  # Hadamard en el primer qubit
circuito.cx(0, 1)  # CNOT para generar el estado de Bell

# PASO 2: ALICE CODIFICA LOS BITS CLÁSICOS EN SU QUBIT
bits_a_enviar = "11"  # Prueba con otros valores: "00", "01", "10", "11"

print(f"\n🔹 Alice quiere enviar los bits: {bits_a_enviar}")

if bits_a_enviar == "01":
    circuito.x(0)  # Aplica X si el primer bit es 1
elif bits_a_enviar == "10":
    circuito.z(0)  # Aplica Z si el segundo bit es 1
elif bits_a_enviar == "11":
    circuito.x(0)
    circuito.z(0)  # Aplica X y Z si ambos bits son 1

# PASO 3: BOB DECODIFICA EL MENSAJE
circuito.cx(0, 1)  # Deshace el entrelazamiento
circuito.h(0)  # Hadamard en el primer qubit

# PASO 4: MEDICIÓN (ajuste en el orden de los bits)
circuito.measure([0, 1], [1, 0])  # Invertimos el orden de los bits clásicos

# SIMULACIÓN CON AerSimulator
simulador = AerSimulator()
circuito_transpilado = transpile(circuito, simulador)
resultado = simulador.run(circuito_transpilado, shots=1024).result()
cuentas = resultado.get_counts()

# OBTENER LOS BITS RECIBIDOS POR BOB
bits_recibidos = max(cuentas, key=cuentas.get)

print("\n🔹 Circuito cuántico:")
print(circuito.draw())

print("\n🔹 Resultados de la medición:")
for key, value in cuentas.items():
    print(f"  {key} → {value} veces")

# Mostrar los bits corregidos
print(f"\n✅ Bob ha recibido los bits: {bits_recibidos}")
print(f"✅ Coinciden con los bits originales de Alice: {'Sí' if bits_recibidos == bits_a_enviar else 'No'}")


print(f"\n✅ Bob ha recibido los bits: {bits_recibidos}")
print(f"✅ Coinciden con los bits originales de Alice: {'Sí' if bits_recibidos == bits_a_enviar else 'No'}")
