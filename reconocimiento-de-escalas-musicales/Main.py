import py_midicsv as pm
from Comparator import Comparator

# Se cambia el formato del archivo de MIDI a CSV
OnRepeat = pm.midi_to_csv(r"C:\Users\Familia\Desktop\Santiago\UNIVERSIDAD\Semestre IV\Matematicas Discretas II\Proyecto\OnRepeat.mid")

# Extraccion de Notas de Archivo MIDI
notes = []
for l in OnRepeat:
	line = l.split(",")
	if len(line)>=5:
		if line[2] == " Note_on_c":
			m = int(line[4])
			notes.append(m)

"""
C  C# D  D# E  F  F# G  G# A  A# B  
0  1  2  3  4  5  6  7  8  9  10 11
"""

majorComp = Comparator([0,2,4,5,7,9,11])
notesStr = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

indiceMayor = majorComp.analyze(notes)
print("Indices Escala Mayor", indiceMayor)
print("\nEscala:", notesStr[ indiceMayor.index( max(indiceMayor) ) ], "mayor\n" )