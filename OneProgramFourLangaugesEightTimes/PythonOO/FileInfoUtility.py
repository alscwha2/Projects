import sys
args = sys.argv

def check_args():
	proper_syntax_message = """improper usage
	proper usage:
		grep <STRING> <FILE>
		wc <FILE>
		grep <STRING> <FILE> | wc
	"""
	number_of_args = len(args)
	global command
	global file_name
	global grep_string
	if number_of_args == 3:
		if args[1].lower() != "wc":
			raise SyntaxError(proper_syntax_message)
		else:
			command = "wc"
			file_name = args[2]
	elif number_of_args == 4:
		if args[1].lower() != "grep":
			raise SyntaxError(proper_syntax_message)
		else:
			command = "grep"
			grep_string = args[2]
			file_name = args[3]
	elif number_of_args == 6:
		if args[1].lower() != "grep" or args[4]!= "|" or args[5].lower() != "wc":
			raise SyntaxError(proper_syntax_message)
		else:
			command = "grepwc"
			grep_string = args[2]
			file_name = args[3]
	else:
		raise SyntaxError(proper_syntax_message)

check_args()

class DocumentProcessorBuilder:
	def build(self):
		processor = DocumentProcessor()

		try:
			processor.LineFilterer = self.LineFilterer
		except AttributeError:
			pass
		try:
			processor.CaseConverter = self.CaseConverter
			processor.WordFinder = self.WordFinder
			processor.NonABCFilterer = self.NonABCFilterer
			processor.WordCounter = self.WordCounter
		except AttributeError:
			pass

		return processor

class DocumentProcessor:
	def process(self, file_contents):
		lines = file_contents.splitlines()
		words_and_count = ""
		try:
			lines = self.LineFilterer.process(lines)
		except AttributeError:
			pass
		try:
			lines = self.CaseConverter.process(lines)
			words = self.WordFinder.process(lines)
			words = self.NonABCFilterer.process(words)
			words_and_count = self.WordCounter.process(words)
			for word, count in words_and_count.items():
				print("%s - %s" %(word,count))
			return
		except AttributeError:
			pass
		for line in lines:
			print(line)

class LineFilterer:
	def __init__(self, grep_string):
		self.grep_string = grep_string

	def process(self, lines):
		return [line for line in lines if self.grep_string in line]

class CaseConverter:
	def process(self, lines):
		return [line.lower() for line in lines]

class WordFinder:
	def process(self, lines):
		words = []
		for line in lines:
			words[len(words):] = line.split()
		return words

class NonABCFilterer:
	def process(self, words):
		def is_alpha_numeric(char):
			return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		def is_not_blank(str):
			return str != ""
		new_words = []
		for word in words:
			string = ""
			for char in filter(is_alpha_numeric, word):
				string += char
			new_words.append(string)
		words = []
		for word in filter(is_not_blank, new_words):
			words.append(word)
		return words

class WordCounter:
	def process(self, words):
		words_and_count = {}
		for word in words:
			try:
				words_and_count[word] = words_and_count[word] + 1
			except KeyError:
				words_and_count[word] = 1
		return words_and_count

file_contents = ""
with open(file_name) as file:
	file_contents = file.read()

builder = DocumentProcessorBuilder()
if command in ["grep", "grepwc"]:
	builder.LineFilterer = LineFilterer(grep_string)
if command in ["wc", "grepwc"]:
	builder.CaseConverter = CaseConverter()
	builder.WordFinder = WordFinder()
	builder.NonABCFilterer = NonABCFilterer()
	builder.WordCounter = WordCounter()
documentProcessor = builder.build()
documentProcessor.process(file_contents)