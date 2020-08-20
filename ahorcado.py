import random
from imagenes_ahorcado import *
import os


#importando palabras
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
lista_palabras = []
with open('palabras.txt', 'r') as file:
       lista_palabras = [line.strip().upper() for line in file]



class Ahorcado:
	def __init__(self):
		self.palabra_adivinar = ""
		self.palabra_acertada_puntos = 0
		self.intentos = 0
		self.vidas = 3
		self.puntos = 0
		self.letras_ingresadas = " "
		self.jugar = True
		self.generarNuevo = False


	def palabra_nueva(self):
		self.palabra_adivinar = lista_palabras[random.randint(0,49)]


	def retornar_jugar(self):
		return self.jugar


	def retornar_vida(self):
		vida = ["*",
				"* *",
				"* * *",]
		return vida[self.vidas-1]


	def retornar_puntos(self):
		return self.puntos


	def retornar_guiones(self):
		texto = ""
		for i in self.palabra_adivinar:
			if i in self.letras_ingresadas:
				texto += i + " "
			else:
				texto += "- "
		return texto.strip()


	def retornar_figura(self):
		return img_ahorcado[self.intentos]


	def menu_ahorcado(self):
		texto = "\t\tJuego del Ahorcado\n"
		texto += "---- ---- ---- ---- ---- ---- ---- ---- ----\n"
		texto += f"|Vida: {self.retornar_vida()}|\t|Puntos: {self.retornar_puntos()}|\t|Intentos: {self.intentos}|\n"
		texto += "\n \n"
		texto += f"{self.retornar_guiones()}\n"
		texto += f"{self.retornar_figura()}\n"
		return texto


	def ingresar_letra(self):
		letra = input("Ingresa una Letra: \n|: ").upper().strip()
		if len(letra) > 1:
			return self.comprobar_palabra(letra)
		else:
			return self.comprobar_letra(letra)


	def comprobar_palabra(self, palabra):
		if palabra == self.palabra_adivinar:
			self.puntos_positivos(1000)
			return "Acertado!!!"
		else:
			self.puntos_negativos()
			return "Error!"


	def comprobar_letra(self, letra):
		if letra in self.letras_ingresadas:
			return "Letra Ya Ha Sido Ingresada"

		if letra in abecedario:
			self.letras_ingresadas += letra
			if letra in self.palabra_adivinar:
				numero_letras = self.palabra_adivinar.count(letra)
				self.puntos_positivos(10, numero_letras)
				return "Acertado!"
			else:
				self.puntos_negativos()
				return "Error!"
		else:
			self.puntos_negativos()
			return "Letra Ingresada no Es Valida"


	def puntos_negativos(self):
		self.intentos += 1
		if self.intentos == 7:
			self.intentos = 0
			self.vidas -= 1
			self.generarNuevo = True
			if self.vidas == 0:
				self.convertir_false()


	def convertir_false(self):
		self.jugar = False


	def puntos_positivos(self, numero, numero_letras=1):
		if numero == 10:
			self.puntos += 10 * numero_letras
			self.palabra_acertada_puntos += numero_letras
		else:
			self.puntos += (len(self.palabra_adivinar) - self.palabra_acertada_puntos) * 10
			self.palabra_acertada_puntos += len(self.palabra_adivinar) - self.palabra_acertada_puntos


	def palabras_acertadas_comprobar(self):
		if self.palabra_acertada_puntos == len(self.palabra_adivinar):
			return True
		else:
			return False
	
		
	def nuevaPalabra(self):
		self.palabra_acertada_puntos = 0
		self.letras_ingresadas = " "
		self.intentos = 0


	def nuevo_intento(self):
		if self.generarNuevo:
			self.generarNuevo = False
			return self.generarNuevo
		return not self.generarNuevo


hola = Ahorcado()
while hola.jugar:
	os.system("cls")
	hola.palabra_nueva()
	while not hola.palabras_acertadas_comprobar() and hola.nuevo_intento():
		print(hola.menu_ahorcado())
		print(hola.ingresar_letra())
		os.system("cls")
	hola.nuevaPalabra()
print("fin del juego")