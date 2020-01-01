import src.Status as Status

class Cigar:

	def get_mapping_status(self, read):
		if read['CIGAR'] == "100M":
			return Status.Status.MAPPED
		elif read['CIGAR'] == "*":
			return Status.Status.UNMAPPED
		else:
			return Status.Status.PARTIAL
