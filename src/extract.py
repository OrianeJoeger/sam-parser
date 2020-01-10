import csv

def run_pair(file):
	paire = []
	tmp_reads = {}
	
	with open(file) as sam_file:
		sam_reader = csv.reader(sam_file, delimiter='\t')
		for row in sam_reader:
			if not row[0].startswith("@"):
				read = dict(
					QNAME = row[0],
					FLAG = row[1],
					RNAME = row[2],
					POS = row[3],
					MAPQ = row[4],
					CIGAR = row[5],
					RNEXT = row[6],
					PNEXT = row[7],
					TLEN = row[8],
					SEQ = row[9],
					QUAL = row[10])
				pos = read['POS']
				pnext = read['PNEXT']

				if pnext in tmp_reads:
					yield [read, tmp_reads[pnext]]
					del tmp_reads[pnext]
				else:
					tmp_reads[pos] = read