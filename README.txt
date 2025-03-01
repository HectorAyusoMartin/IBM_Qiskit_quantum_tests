Pruebas de programación Cuántica. Qiskit. IBM.
Héctor Ayuso Martín.


Este repositorio contiene una serie de cuadernillos Jupyter Notebook con programación cuántica, utilizando la libreria de IBM denominada Qiskit.
La idea de este repositorio es demostrar y visualizar conceptos de la física cuántica aplicada a la computación, y sobre todo, la documentación de dichos experimentos, en el ejericicio
de disponer de mas documentación en Castellano.
Los conceptos aplicados en este repositorio son de un nivel iniciación , como resultado de mi propia inquietud sobre la computación cuántica, a raiz de un showcase de Microsoft Majorana 1
realizado un par de días antes de la escritura de este readme.txt.

En el primer Notebook, se experimenta y se grafica el resultado de colocar un qbit en superposición cuántica, entrelazarlo con otro qubit, realizar una medición y graficar su colapso en probabilidades.
El experimento final es la creación de un circuito con 100 qubits en estado GHZ, en superposición cuántica, y con entrelazamiento todos ellos. Se envia el ciercuito a una QPU real de IBM en Alemania, 
y se estudian sus resultados.



Actualmente, y en el uso de el entorno virtual .venv en este repositorio, el simulador Aer tiene problemas de estabilidad e importación, sigo trabajando en solucionarlo para documentar una forma
funcional de poder importar dicho módulo de simulación en un entorno Windows.
Hasta el momento, sin tener estabilidad en el uso de qiskit-Aer, el cuadernillo dispone de un circuito de tres qubits y tres bits clásicos, diferentes tipos de puertas cuánticas en formato 
Single-Q y Mult-Q, para observar y cuantificar de forma estadística los diferentes estados de qbits y printearlos en distintos tipos de grafos utilizando la librería Matplotlib.
La idea principal de este repositorio es la documentación de dicha algorítmia, en forma de iniciación a la libreria de IBM Qiskit.




TODO: Implementacióin de Qiskit-Aer inestable. Se ha configurado un .venv con Py 3.10, evitando así su uso en Py 3.12, pero sigue con problemas de estabilidad e importación.

En el cuadernillo 1, entrelazamiento_cuántico, por los problemas de inestabilidad y dificultad en la importación del simulador Qiskit-Aer mencionado anteriormente, se optó por la ejecución real
del código en una QPU real de IBM en Alemania.

