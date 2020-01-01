import src.Status as Status
import csv

class Flag:

	def __init__(self):
		self.liste_format_sam = []
		self.description_flag = {}

		with open('data/sam_format.csv') as format_file:
			format_reader = csv.reader(format_file, delimiter = ';')
			for row in format_reader:
				elem = dict(id = row[0], decimal = row[1], description = row[2])
				self.liste_format_sam.append(elem)

	#Retourne l'element contenant le decimal le plus proche du flag
	def get_closest(self, nbr):
		save_elem = None

		for elem in self.liste_format_sam:
			if (save_elem == None and nbr >= int(elem['decimal'])):
				save_elem = elem
		return save_elem

	def set_description_flag(self, flag):
		read_descriptions = []
		is_mapped = True
		nbr = flag

		while (nbr > 0):
			elem = self.get_closest(nbr)
			read_descriptions.append(elem['description'])
			nbr = nbr - int(elem['decimal'])
			if (int(elem['decimal']) == 4):
				is_mapped = False
		self.description_flag[flag] = dict(flag = flag, description = read_descriptions, mapped = is_mapped)

	def get_mapping_status(self, read):
		flag = int(read['FLAG'])
		if (flag not in self.description_flag):
			self.set_description_flag(flag)
		return self.description_flag[flag]['mapped']