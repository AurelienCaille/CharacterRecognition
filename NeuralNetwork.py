#!/usr/bin/env python3
import random
import numpy as np
from pprint import pprint
class Neurone:
	def __init__(self, nb_of_entry, weights = [], seuil = 0):
		if weights == []:
			self.weights = [random.random() for i in range(nb_of_entry)]
			self.seuil = random.random()
		else:
			self.weights = weights
			self.seuil = seuil
	
	def multiply(self, liste):
	
		result = []
		if len(liste) != len(self.weights):
			raise ValueError("error incorect len of liste")
		for pos in range(len(liste)):
			result.append(liste[pos]*self.weights[pos])
		return result
	
	def run(self, liste):
	
		if sum(self.multiply(liste)) > self.seuil:
			return 1
		else:
			return 0
	def __repr__(self):
		string = "Neurone(1, ["
		for weight in self.weights:
			string = string + str(weight) + ", "
		string = string[:-2]+ "]"
		string = string + ", "  + str(self.seuil)
		return string + ")"

class NeuralNetwork:
	def __init__(self, inpt = [], hidden = [], output = []):
		if inpt == []:
			self.input = [Neurone(1) for i in range(2)]
			self.hidden = [Neurone(2) for i in range(3)]
			self.output = [Neurone(3) for i in range(1)]
		else:
			self.input = inpt
			self.hidden = hidden
			self.output = output
	def run(self, liste):
		if len(liste) != len(self.input):
			raise ValueError("incorrect len")
		tmp = []
		
		for pos in range(len(self.input)):
			if self.input[pos].run(liste[pos]) == 1:
				tmp.append(1)
			else:
				tmp.append(0)
		tmp1 = []
		for neurone in self.hidden:
			if neurone.run(tmp) == 1:
				tmp1.append(1)
			else:
				tmp1.append(0)
		result = []
		for neurone in self.output:
			if neurone.run(tmp1) == 1:
				result.append(1)
			else:
				result.append(0)
		return result
		
	def croisement(self, neuralnetwork):
		
		
		
		
	def __repr__(self):

		string = "-----input-----\n"
		for neurone in self.input:
			string = string + str(neurone) + "\n"
		string = string + "-----hidden ----\n"
		for neurone in self.hidden:
			string = string + str(neurone) + "\n"
		string = string + "----output----\n"
		for neurone in self.output:
			string = string + str(neurone) + "\n"
		
		return string

class Population:
	def __init__(self):
		self.population = [NeuralNetwork() for i in range(5)]
		
	def run(self, liste, answer):
		result = []
		for neuralnetwork in self.population:
			tmp = neuralnetwork.run(liste)
			if tmp == [answer]:
				result.append(1)
			else:
				result.append(0)
		return result
		
	def evolution(self):
		a = np.array(self.run([[1], [1]], 1))
		b = np.array(self.run([[1], [0]], 0))
		c = np.array(self.run([[0], [1]], 0))
		d = np.array(self.run([[0], [0]], 0))

		somme = a + b + c + d
		maxi = max(somme)
		print (maxi)
		meilleur = []
		for pos in range(len(self.population)):
			if somme[pos] == maxi:
				meilleur.append(self.population[pos])
		
		new_pop = meilleur + [NeuralNetwork() for i in range(len(self.population) - len(meilleur))]
		
		self.population = new_pop
if __name__ == "__main__":
	A = Population()
	A.evolution()
	
	
