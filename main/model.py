import numpy
from qiskit import QuantumCircuit,transpile, Aer
from math import pi
from pylatexenc import *

class CircuitGridModel:
    def __init__(self):
        
        self.clear_circuit_move()
        self.clear_circuit_fight()

    def clear_circuit_move(self):
    # Also creates circuit. Will call this every round so collapse_circuit doesn't 
    # get messed up

        # created with all three states in a superposition
        self.qwl = QuantumCircuit(3)
        self.qwl.clear()
        self.qwl.h(0)
        self.qwl.h(1)
        self.qwl.h(2)

    def clear_circuit_fight(self):
    # Also creates circuit. Will call this every round so collapse_circuit doesn't 
    # get messed up. This is a two-state quantum circuit, specifically created for 
    # fighting scenes.
    
    # created without a superposition. Line 2 has a not gate.
        self.qwlf = QuantumCircuit(2)
        self.qwlf.clear()
        self.qwlf.i(0)
        self.qwlf.x(1)

        qoutput = "Clearing circuit..."
        # print(qoutput)

    def add_to_circuit(self,qin, qcircuit, isFight):
        try:
            if isFight: qtype = self.qwlf
            if not isFight: qtype = self.qwl
        except:
            qoutput = "Something went wrong. Input was "+isFight
            # print(qoutput)

        # qin = qin.upper()
        if qin == "H":
            qtype.h(qcircuit)
        # change output display
        elif qin == "I":
            qtype.i(qcircuit)
        # change output display
        elif qin == "S":
            qtype.s(qcircuit)
        # change output display
        elif qin == "T":
            qtype.t(qcircuit)
        # change output display
        elif qin == "X":
            qtype.x(qcircuit)
        # change output display
        elif qin == "Y":
            qtype.ry(pi/2, qcircuit)
        # change output display
        elif qin == "Z":
            qtype.rz(pi/2, qcircuit)
        # change output display
        else:
        # don't change the output display
            qoutput = qin+" is not a valid input. The valid inputs are: H, I, S, T, X, Y, Z."
            # print(qoutput)
            return 'error'

        # # calls the function that collapses and reads the created circuit.
        # if qcircuit >= (qtype.width() - 1):
        #     if not isFight: self.read_collapsed_circuit_move()
        #     else: self.read_collapsed_circuit_fight()
        

    def collapse(self,qtype):
        # Observes and collapses current circuit. Returns binary list.

        qoutput = "Collapsing circuit..."
        # print(qoutput)

        qtype.measure_all()

        # Transpile for simulator
        simulator = Aer.get_backend('aer_simulator')
        qtype = transpile(qtype, simulator)

        result = simulator.run(qtype, shots=1, memory=True).result()
        memory = result.get_memory(qtype)

        qoutput = "Circuit was observed as "+memory[0]
        # print(qoutput)

        return memory[0]

    def update(self):
        self.clear_circuit_move()
        self.clear_circuit_fight()