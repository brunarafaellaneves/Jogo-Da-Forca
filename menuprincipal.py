#######################################################
# Python Version: 3.10.2							  #
# Autora: Bruna Rafaella Neves | 15/02/2022			  #
# https://www.linkedin.com/in/brunarafaellaneves/	  #
# https://github.com/brunarafaellaneves/Jogo-Da-Forca #
#######################################################

from jogodaforca import JogoDaForca

class MenuPrincipal:
	def __init__(self):
		print("### Jogo da Forca ### \n")
		print("[1] Jogar\n")
		print("[2] Instruções\n\n")
		opcao = input("Escolha uma opção:")

		if (int(opcao) == 1):
			JogoDaForca()
		if (int(opcao) == 2):
			print("XXXXXXXXXXXXXXXXXXXXXXX")
