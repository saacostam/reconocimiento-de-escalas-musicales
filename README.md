# Reconocimiento-de-Escalas-Musicales
Programa, escrito en python, que, mediante aritmética modular, busca clasificar una composición dentro de cierto tipo de escala musical. Este es un proyecto de clase para Matemáticas Discretas.

Program, written in python, that, by means of modular arithmetic, seeks to classify a composition within a certain type of musical scale. This is class project for Discrete Mathematics.

<hr>

# Introduccion
## Problema
Este proyecto busca aplicar la relacion entre la teoria musical y la aritmetica modular para crear un programa de reconocimiento de escalas musicales de acuerdo a un archivo MIDI. Es decir, dado cierto conjunto de notas, traducir dicha información con aritmética modular para facilitar la clasificación de ese conjunto de notas dentro de una escala musical.

# Materiales y Metodo

## Descripcion de los Datos

Los Datos utilizados se extraeran de un archivo MIDI.

#### Wikipedia-MIDI:
"MIDI (abreviatura de Musical Instrument Digital Interface) es un estándar tecnológico que describe un protocolo, una interfaz digital y conectores que permiten que varios instrumentos musicales electrónicos, ordenadores y otros dispositivos relacionados se conecten y comuniquen entre sí."

La caracteristica que nos interesa de los archivos MIDI es este tipo de archivo guarda información acerca de las notas que se reproducen en cierta composición/ presentación musical.

A continuacion un ejemplos de como se almacena informacion dentro de un archivo MIDI:

```
0, 0, Header, 1, 2, 96
1, 0, Start_track
1, 0, Tempo, 468750
1, 0, Time_signature, 4, 2, 24, 8
1, 0, End_track
2, 0, Start_track
2, 0, Title_t, "FL Keys 1"       
2, 0, Note_on_c, 0, 84, 100      
2, 0, Note_on_c, 0, 69, 100      
2, 0, Note_on_c, 0, 60, 100      
2, 0, Note_on_c, 0, 53, 100
2, 0, Note_on_c, 0, 41, 100
2, 72, Note_off_c, 0, 84, 64
2, 72, Note_off_c, 0, 69, 64
(...)
2, 1488, Note_on_c, 0, 38, 100
2, 1488, Note_on_c, 0, 79, 100
2, 1536, Note_off_c, 0, 65, 64
2, 1536, Note_off_c, 0, 57, 64
2, 1536, Note_off_c, 0, 50, 64
2, 1536, Note_off_c, 0, 38, 64
2, 1536, Note_off_c, 0, 79, 64
2, 1536, End_track
0, 0, End_of_file
```

La informacion que nos interesa esta en el quinto espacio de cada linea, el cual coincide con la nota que se reproduce en cierto momento:
```
2, 1488, Note_on_c, 0, 38, 100 ---> 38
```
Los archivos MIDI guardan el tiempo cuando se presiono y cuando se solto la tecla en un piano roll, por lo cual solo se consideraran las notas que esten en una linea que indique "Note_on_c".

## Descripcion de Algoritmo (Metodos)

### Notas Musicales y Octavas
Las notas musicales, segun la notacion de la musica occidental, son A, A#, B, C, C#, D, D#, E, F, F#, G, G#. La distancia entres dos notas adyacentes se conoce como semitono. Por ejemplo, la distancia entre C y C# es de un semitono.

Estas notas musicales estan presentes a diferentes octavas. Es decir, si toco la nota C en un piano y subo/bajo 12 semitonos (o teclas de piano) vuelvo a caer en C. 

### Escalas Musicales

Toda composición, entendida como un conjunto de notas arbitrarias, se puede clasificar dentro de escalas musicales. Las escalas musicales son conjuntos de notas que, sin irse mucho a la teoría musical, suenan bien juntas y generan cierto tipo de emoción.

Estas escalas son generadas de acuerdo a una nota base (o tonica), y las notas que estén a ciertos intervalos de dicha nota. 

Es importante aclarar que, en la practica, las composiciones musicales no se apegan completamente a cierta escala, puesto que estas variaciones pueden ser mas llamativas al oyente harmonicamente. Es decir, puede que una composicion utilize notas fuera de cierta escala, pero se clasifique dentro de dicha escala.

## Descripcion de los Metodos

## Relacion Artimetica Modular con Teoria Musical

### Aritmetica Modular en la Teoria Musical
La naturaleza ciclica de las notas musicales, organizadas en un piano roll, apuntan a la relacion entre la aritmetica modular y la teoria musical. 

- "Several fundamental notations of number theory arise in music theory".

Si enumeramos un piano roll, como se muestra en la siguiente imagen,  como medio de organizar las relaciones de tono:

dos notas que estan a n octavas de distancia, que suenan similar al oido, y se clasifican como la misma nota musical, se puedan entender mediante:

$$
\begin{align*}
  y-x &= 12k\\
\end{align*}
$$

por lo cual x es congruente con y mod 12.

$$
\begin{align*}
  y &= x\space(mod 12)\\
\end{align*}
$$

### Clases de tono (Pitch Classes)

Aplicando el concepto de clase de congruencia a la musica obtenemos el concepto de clases de tono. Todas las notas dentro del piano roll que se clasifican como cierta nota son resultado de la clase de congruenica de 

$$
\begin{align*}
  [n]_{12}\\
\end{align*}
$$

siendo n el menor residuo de la clase de congruencia correspondiente a ese tono.

### Escalas desde la Artimetica Modular

Una escala es una disposición específica de ocho tonos separados a ciertos intervalos relativos a una nota musical base (o tonica). Por ejemplo, la escala mayor de C es:

$$
\begin{align*}
  0, 2, 4, 5, 7, 9, 11, 12\\
\end{align*}
$$

La escala anterior corresponde unicamente con la primera octava; si se quiere obtener todas las posiciones del piano roll donde la escala mayor de C es presente se debe repetir el anterior procedimiento siendo 12 la tonica, y luego 24, y asi sucesivamente. Sin embargo, si vemos la anterior escala bajo la lupa de la aritmetica modular (mod 12) podemos entender la escala mayor de C simplemente como:

$$
\begin{align*}
  0, 2, 4, 5, 7, 9, 11\\
\end{align*}
$$

Otro ejemplo, si queremos hallar la escala de G#:

$$
\begin{align*}
  8, 10, 12, 13, 15, 17, 19, 20\\
\end{align*}
$$

Ahora, si lo vemos desde la aritmetica modular:

$$
\begin{align*}
  8, 10, 12, 1, 3, 5, 7\\
\end{align*}
$$

El proceso anterior permite simplificar lo que podria ser un gran conjunto de notas musicales a simplemente 7 notas musicales.

Fuente: https://foresthillshs.enschool.org/ourpages/auto/2011/11/2/74617344/Number%20Theory%20and%20Music.pdf

## Descripcion de los Metodos

## Metodos utilizados

### Extraccion de Datos

Se utiliza la libreria py_midicsv con el proposito de leer el archivo MIDI

```
import py_midicsv as pm

# Se cambia el formato del archivo de MIDI a CSV
song = pm.midi_to_csv(r"C:\Users\Familia\Desktop\Santiago\UNIVERSIDAD\Semestre IV\Matematicas Discretas II\Proyecto\OnRepeat.mid")

# Extraccion de Notas de Archivo MIDI
notes = []
for l in song:
	line = l.split(",")
	if len(line)>=5:
		if line[2] == " Note_on_c":
			m = int(line[4])
			notes.append(m)
```
El metodo anterior debe recorrer todo el archivo; y se deben guardar todas las notas debido a la forma como se realizara el analisis de la escala musical (explicada posteriormente). Debido a esto, este metodo trabaja en tiempo lineal.

### Clase Comparator

Se crea un objeto Comparator para facilitar la implementacion de varios tipos de escalas (mayor, menor, etc.); por cada escala musical que se quiera analizar se instancia un objeto Comparator.

```
class Comparator:
```
Como se dijo anteriormente, una composicion puede utilizar notas fuera de su escala. Es por esto que no se debe descartar cierta escala simplemente porque la composicion contiene notas fuera de dicha escala. Es por esto que se realiza el analisis mediante un "factor de coincidencia" el cual es, simplemente, un cociente entre el numero de notas de la composicion que pertenecen a cierta escala y el total de notas de la composicion. El factor correspondiente a cada tonica se guarda en el atributo factors considerando el siguiente orden:
```
Nota:   C  C# D  D# E  F  F# G  G# A  A# B  
Indice: 0  1  2  3  4  5  6  7  8  9  10 11
```
La clase Comparator se inicializa con una lista de enteros que representan los intervalos, relativos a la tonica, relacionados a la construccion de cierto tipo de escala musical. En este sentido, se tiene, por ejemplo, un comparador para escalas mayores, otros para escalas menores, etc. 
```
class Comparator:
	def __init__( self, interval ):
		'''
		El intervalo define el tipo de escala que se va a analizar: mayor, menor, etc.
		'''
		self.interval = interval
		self.factors = []
```

La clase comparator utiliza estos intervalos para constuir la escala con cada nota musical como tonica. Por ejemplo, en el caso de un comparador para escalas mayores, la clase comparator debe generar: C mayor, C# mayor, D mayor...

El metodo buildScale se encarga de generar las escalas de cada nota. El parametro root es un entero donde:

```
Nota: C  C# D  D# E  F  F# G  G# A  A# B  
Int:  0  1  2  3  4  5  6  7  8  9  10 11
```
Como estamos abordando el problema desde la aritmetica modular, y mapearemos cada nota al sistema de minimo residuo modulo 12, solo es necesario generar este sistema; el cual se genera sumandole a root cada numero del intervalo y aplicando (mod 12) al total. El metodo buildScale trabaja en tiempo constante puesto que en el peor de los casos O(12) -> O(1).
```
class Comparator:
	def buildScale( self, root ):
		'''
		Construye la escala dada un nota base (root) y el intervalo.
		Root dado como un numero.
		El intervalo define el tipo de escala: mayor, menor, etc.
		Retorna un set.
		'''

		scaleReturn = set()
		for intervalo in self.interval:
			scaleReturn.add( ( root + intervalo) % 12 )
		return scaleReturn
```
El metodo analyze se encarga de realizar el mapeo de las notas musicales al sistema de minimo residuo modulo 12; y asi compararlas facilmente con cada una de las escalas generadas. El metodo analyze trabaja en tiempo lineal puesto que, debido a la implementacion con "factor de coincidencia", es necesario recorrer todas las notas para acercarse mas al centro tonal de la cancion.
```
class Comparator:
	def analyze( self, notes ):
		for n in range(12):
			scale = self.buildScale(n)
			count = 0
			for note in notes:
				if (note%12) in scale:
					count += 1
			self.factors.append((count/len(notes)))

		return self.factors
```

## Analisis de los metodos utilizados

Se opto por el realizar el analisis por "factor de coincidencia" porque, aunque es mas laborioso computacionalmente, arroja conclusiones mas confiables.

Por ejemplo, otra posible implementacion seria que, al recorrer el archivo, se guarden las notas dentro de un set; simplificando asi el numero de notas que se deben revisar. Sin embargo, debido a que no se pueden repetir notas, al momento de realizar las comparaciones se le daria igual peso a todas las notas, lo cual es problematico puesto que cierta nota que aparece una unica vez tendria la misma importancia que una nota que aparece repetidas veces en la cancion, lo cual incrementa la posibilidad de error.

#### Limitaciones - Posibles Mejoras:
Una composicion pertenece unicamente a cierta escala, puesto que no son unicamente las notas que estan presenten en la composicion las que definen la escala sino tambien la frecuencia de estas. Una composicion que se clasifica como C mayor puede, dentro de este programa, ser clasificada como A menor puesto que estas dos escalas comparten las mismas notas. Si se quisiera mejorar la capacidad del algoritmo para clasificar la composicion a una unica escala es necesario considerar las frecuencias en las que se presenta cada nota y de acuerdo a esto definir el tipo de escala. No obstante, para la implementacion de este proceso no es necesaria la aritmetica modular.

### Video de Prueba

Video de Prueba <a href="https://www.youtube.com/watch?v=_qc90_1MXfU" target="_blank">aqui<a/>!

# Conclusiones

*   La traduccion, mediante aritmetica modular, de una escala musical y del conjunto de notas de una composicion, facilitan el proceso de comparacion cuando se busca clasificar una cancion dentro de una escala musical.

# Referencias

*    'Functions of Number Theory in Music' - Craig M. Johnson
https://foresthillshs.enschool.org/ourpages/auto/2011/11/2/74617344/Number%20Theory%20and%20Music.pdf
"""
