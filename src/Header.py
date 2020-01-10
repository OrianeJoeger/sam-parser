import src.Status as Status
import csv

class Header:

	def __init__(self):
		self.liste_header_sam = {}
		self.headers = {}

		with open('data/sam_format_header.csv') as format_file:
			header_reader = csv.reader(format_file, delimiter = ';')
			for row in header_reader:
				header = row[0]
				tag = row[2]
				elem = dict(header = header, h_description = row[1], tag = tag, t_description = row[3])
				
				if header not in self.liste_header_sam:
					self.liste_header_sam[header] = {}

				self.liste_header_sam[header][tag] = elem

	def load_format_header(self, file):
		with open(file) as sam_file:
			sam_reader = csv.reader(sam_file, delimiter='\t')
			for row in sam_reader:
				if row[0].startswith("@"):
					section = row[0][1:]
					if row[0] not in self.headers:
						self.headers[section] = {}

					for cell in row[1:]:
						parts = str(cell).split(':', maxsplit=1)
						self.headers[section][parts[0]] = parts[1]
				else:
					return;

	def print(self):
		print('HEADER')
		print('================================')
		for section, values in self.headers.items():
			print(self.liste_header_sam[section]['']['h_description'])
			print('--------------------------------')
			for name, value in values.items():
				print(self.liste_header_sam[section][name]['t_description'], ':', value)

			print('')