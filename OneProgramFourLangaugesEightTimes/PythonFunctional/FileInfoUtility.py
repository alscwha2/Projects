from sys import argv
from functools import reduce
from re import sub

# FUNCTION DEFINITIONS

def check_args():
	"""Enforces Proper Syntax"""
	proper_syntax_message = """improper usage
	proper usage:
		grep <STRING> <FILE>
		wc <FILE>
		grep <STRING> <FILE> | wc
	"""
	number_of_args = len(argv)
	global command
	global file_name
	global grep_string
	if number_of_args == 3:
		if argv[1].lower() != "wc":
			raise SyntaxError(proper_syntax_message)
		else:
			command = "wc"
			file_name = argv[2]
	elif number_of_args == 4:
		if argv[1].lower() != "grep":
			raise SyntaxError(proper_syntax_message)
		else:
			command = "grep"
			grep_string = argv[2]
			file_name = argv[3]
	elif number_of_args == 6:
		if argv[1].lower() != "grep" or argv[4]!= "|" or argv[5].lower() != "wc":
			raise SyntaxError(proper_syntax_message)
		else:
			command = "grepwc"
			grep_string = argv[2]
			file_name = argv[3]
	else:
		raise SyntaxError(proper_syntax_message)

def count_words(dic, word):
	if not isinstance(dic, dict):
		return {dic : 1, word : 1}
	try:
		dic[word] = dic[word] + 1
	except Exception:
		dic[word] = 1
	return dic

def print_count(dic):
	for word, count in dic.items():
		print('%s - %s' %(word,count))

def print_lines(lines):
	for line in lines:
		print(line)


# PROGRAM EXECUTION
check_args() #note that I took the liberty to use side-effects in this trivial function call

file_contents = ""
with open(file_name) as file: file_contents = file.read()

lines = file_contents.splitlines()
if command in ["grep", "grepwc"]:
	lines = list(filter(lambda line: grep_string in line, lines))   		#FilterLines
if command in ["wc", "grepwc"]:
	print_count(															#print WC results
		reduce(count_words, 												#CountWords
			[{}] + list(filter(lambda string : string != "", 				#delete empty strings
				list(map(lambda string : sub("[^0-9A-Za-z]", "", string), 	#NonABCConverter
					reduce(lambda a,b : a + b.split(), 						#FindWords
						[[]] + list(map(str.lower, lines))))))))) 			#ConvertCase
if command in ["grep"]: print_lines(lines)