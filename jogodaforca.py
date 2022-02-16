#######################################################
# Python Version: 3.10.2							  #
# Autora: Bruna Rafaella Neves | 15/02/2022			  #
# https://www.linkedin.com/in/brunarafaellaneves/	  #
# https://github.com/brunarafaellaneves/Jogo-Da-Forca #
#######################################################

import json
from random import randint

class JogoDaForca:
	def __init__(self):
		self.palavra = ''
		self.dicas = []
		self.chances_restantes = 6
		self.fim_de_jogo = False
		self.letras_descobertas = []
		self.categoria = ''

		## apenas para visualização - estudar novas maneiras de fazer
		self.boneco = ['O','/','|','\\','/','\\']

		self.escolhercategoria()
		self.iniciarjogo()

	def escolhercategoria(self):
		print("\n # Categorias # \n")
		print("[1] Animais \n")
		print("[2] Comidas \n")
		print("[3] Cores \n\n")
		categoria = int(input("Escolha uma categoria:"))

		if (categoria == 1):
			self.categoria = 'animais'
		if (categoria == 2):
			self.categoria = 'comidas'
		if (categoria == 3):
			self.categoria = 'cores'

	def iniciarjogo(self):

		self.sortearpalavra()

		## apenas para visualização - estudar novas maneiras de fazer
		self.estadoboneco()
		print("Palavra: ")
		for letra in self.palavra :
		    self.letras_descobertas.append("_")
		    print ("_", end = " ")
		print("\n")

		while (self.fim_de_jogo == False):
			self.recebeletra(self.palavra)
			for x in self.letras_descobertas:
				print (x, end = " ")

			if (self.letras_descobertas == self.palavra):
				self.fimdejogo()

	def recebeletra(self, palavra):
		letrarecebida = str(input("Digite a letra: ")).strip().lower()

		if letrarecebida in palavra:
			self.acertouletra(letrarecebida)
		else:
			self.errouletra()
		self.estadoboneco()

	def sortearpalavra(self):

		with open("informacoes_forca.json", "r", encoding='utf-8') as json_file:
			dados = json.load(json_file)
			dicionario = dados['categoria']
			palavras_por_categ = dicionario[self.categoria]
		qt_palavras = len(palavras_por_categ)-1
		numero_aleatorio = randint(0, qt_palavras)
		self.palavra = list(palavras_por_categ[numero_aleatorio]['palavra'])
		self.dicas = palavras_por_categ[numero_aleatorio]['dicas']

	def errouletra(self):
		self.chances_restantes-=1
		self.boneco[self.chances_restantes] = "X"
		if (self.chances_restantes == 0):
			self.fimdejogo(True)

	def acertouletra(self, letrarecebida):
		x = 0
		for letra in self.palavra:
				if (letrarecebida == letra):
					self.letras_descobertas[x] = letra
				x+=1

	def fimdejogo(self, perdeu=False):
		if (perdeu == False):
			print("Parabéns! Você conseguiu!!!")
		else:
			print("perdeu!!!")
		self.fim_de_jogo = True

	def estadoboneco(self):
		print(" {} \n{}{}{}\n{} {}".format(self.boneco[0],
										   self.boneco[1],
										   self.boneco[2],
										   self.boneco[3],
										   self.boneco[4],
										   self.boneco[5]))
		print("Chances Restantes: {}".format(self.chances_restantes))