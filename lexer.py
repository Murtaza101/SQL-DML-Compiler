import re
class Lexer(object):
	def __init__(self, source_code):
		self.source_code = source_code 

	def tokenize(self):
		
		# where all the tokens created by lexer will be stored
		tokens = []

		# Create a word list of the source code
		source_code = re.split('\t+|\s+|\n+|(\(|\)|\{|\}|,|;|\[|\])',self.source_code)
		
		# tracking indexes
		source_index = 0
		
		# loop through each word in source code
		while source_index < len(source_code):
			if source_code[source_index] is not None:
				print(source_code[source_index])
			# increases word index after checking it
			source_index += 1
		# return created tokens
		return tokens