class Status :
	UNMAPPED = 0
	MAPPED = 1
	PARTIAL = 2

	def __init__(self):
		self.__reads = {
			self.UNMAPPED: 0,
			self.MAPPED: 0,
			self.PARTIAL: 0
		}
		self.__pairs = {
			self.MAPPED: {
				self.UNMAPPED: 0,
				self.MAPPED: 0,
				self.PARTIAL: 0
			},
			self.PARTIAL: {
				self.UNMAPPED: 0,
				self.PARTIAL: 0
			},
			self.UNMAPPED: {
				self.UNMAPPED: 0
			}
		}

	def push(self,a,b):
		self.__reads[a] += 1
		self.__reads[b] += 1

		if a == self.MAPPED:
			self.__pairs[a][b] +=1
		elif b == self.MAPPED:
			self.__pairs[b][a] +=1
		elif a == self.PARTIAL:
			self.__pairs[a][b] +=1
		else:
			self.__pairs[b][a] +=1



	def print(self):
		print("Il y a " + str(self.__reads[self.MAPPED]) + " reads mappés")
		print("Il y a " + str(self.__reads[self.PARTIAL]) + " reads partiellement mappés")	
		print("Il y a " + str(self.__reads[self.PARTIAL]) + " reads non mappé")
		print("Il y a " + str(self.__pairs[self.MAPPED][self.MAPPED]) + " paire de reads parfaitement mappé")
		print("Il y a " + str(self.__pairs[self.PARTIAL][self.PARTIAL]) + " paire de reads partiellement mappé")
		print("Il y a " + str(self.__pairs[self.UNMAPPED][self.UNMAPPED]) + " paire de reads non mappé")
		print("Il y a " + str(self.__pairs[self.MAPPED][self.PARTIAL]) + " paire de reads dont l'un est parfaitement mappé et l'autre partiellement mappé")
		print("Il y a " + str(self.__pairs[self.MAPPED][self.UNMAPPED]) + " paire de reads dont l'un est parfaitement mappé et l'autre non mappé")
		print("Il y a " + str(self.__pairs[self.PARTIAL][self.UNMAPPED]) + " paire de reads dont l'un est partiellement mappé et l'autre non mappé")