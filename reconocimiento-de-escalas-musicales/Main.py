"""	Main: Archivo que muestra el uso basico de la clase Comparator	    """

# Se utiliza el modulo py_midicsv para extraer las notas desde un archivo MIDI.
import py_midicsv as pm
# Sin embargo, lo unico necesario para utilizar esta clase es tener un lista de notas con la notacion en numero de las notas musicales.
from Comparator import Comparator

# Se cambia el formato del archivo de MIDI a CSV
OnRepeat = pm.midi_to_csv(r"dummy.mid")

# Extraccion de Notas de Archivo MIDI
notes = []
for l in OnRepeat:
	line = l.split(",")
	if len(line)>=5:
		if line[2] == " Note_on_c":
			m = int(line[4])
			notes.append(m)

# Se inicializa el objeto de la clase Comparator con los intervalos de la Escala Mayor
majorComp = Comparator([0,2,4,5,7,9,11])
notesStr = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

indiceMayor = majorComp.analyze(notes)
print("Indices Escala Mayor", indiceMayor)
print("\nEscala:", notesStr[ indiceMayor.index( max(indiceMayor) ) ], "mayor\n" )
