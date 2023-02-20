def conjugacionVerbos(palabra):

	pasado = 'io', 'ieron', 'iste', 'i', 'te', 'o', 'aron', 'do', 'aste'
	presente = 'ais', 'es', 'en', 'imos', 'is', 'amos'
	futuro = 'e', 'as', 'a', 'emos', 'eis', 'an'

	if palabra.endswith(tuple(pasado)):
		return 'pasado'
	elif palabra.endswith(tuple(presente)):
		return 'presente'
	elif palabra.endswith(tuple(futuro)):
		return 'futuro'

palabra = "murio"
print("El verbo",palabra,"es de tiempo",conjugacionVerbos(palabra))