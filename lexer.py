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
				word = source_code[source_index]
				# reads SQL keywords 
				if word == ("UPDATE" or "SELECT" or "INTO" or "INSERT" or "DELETE" or "SET" or "CREATE" or "TABLE" or "DISTINCT" or "FROM" or "WHERE" or "AND" or "OR" or "NOT" or 'ORDER' or 'BY' or 'VALUES' or 'IS' or 'NULL' or 'IN' or 'ON' or 'INNER' or 'JOIN' or 'OUTER' or 'LEFT' or 'RIGHT' or '*'): 
					tokens.append(["SQLKeywords",word])
				# reads identifiers
				elif re.match("[a-zA-Z]+\d*",word):
					tokens.append(["Identifier",word])
				# reads integer token
				elif re.match("\d+",word):
					tokens.append(["Integer",word])
				# Comparison Operator token
				elif re.match('<|>|==|>=|<=',word):
					tokens.append(["ComparisonOperator",word])
				# Boolean token
				elif re.match('True|False',word):
					tokens.append(["Boolean",word])
				# Arithmetic Operator token
				elif re.match('=|+|-|/|*',word):
					tokens.append(["Operator",word])
				# Braces token
				elif re.match('{|}|\(|\)|\[|\]',word):
					tokens.append(["Braces",word])	
				# Separators token
				elif re.match(',|;',word):
					tokens.append(["Separator",word])
				# Traditional Programming Language keywords
				elif re.match('if|else|while',word):
					tokens.append(["PLKeywords",word])
				
				
			# increases word index after checking it
			source_index += 1
		# return created tokens
		return tokens
