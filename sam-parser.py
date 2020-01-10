#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import src.extract as Extract
import src.Cigar as Cigar
import src.Flag as Flag
import src.Status as Status

def help():
	print("Utilisation: python3 sam-parser.py [FICHIER] [METHOD]")
	print("[FICHIER] fichier de type type SAM")
	print("[METHOD] la méthode utilisé doit être 'flag' or 'cigar'")

def main():
	if (len(sys.argv) == 3):
		file = sys.argv[1]
		method = sys.argv[2]
		status = Status.Status()

		if (method == "cigar"):
			evaluator = Cigar.Cigar()
		elif (method == "flag"):
			evaluator = Flag.Flag()
		else:
			help()
			exit(1)

		for pair in Extract.run_pair(file):
			status.push(
				evaluator.get_mapping_status(pair[0]),
				evaluator.get_mapping_status(pair[1])
			)
		status.print()
	else:
		help()

main()