class Comparator:
	def __init__( self, interval ):
		"""
		El intervalo define el tipo de escala que se va a analizar: mayor, menor, etc.
		"""
		self.interval = interval
		self.factors = []

	def buildScale( self, root ):
		"""
		Construye la escala dada un nota base (root) y el intervalo.
		Root dado como un numero.
		El intervalo define el tipo de escala: mayor, menor, etc.
		Retorna un set.
		"""

		scaleReturn = set()

		for intervalo in self.interval:
			scaleReturn.add( ( root + intervalo) % 12 )

		return scaleReturn

	def analyze( self, notes ):
		for n in range(12):
			scale = self.buildScale(n)
			count = 0
			for note in notes:
				if (note%12) in scale:
					count += 1
			self.factors.append((count/len(notes)))

		return self.factors