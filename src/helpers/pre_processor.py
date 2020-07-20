# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.stem import PorterStemmer
# from nltk.corpus import stopwords
# from nltk import ngrams
import string, os, math
import PyPDF2

class Preprocessor:
	"""
	Preprocessor class provides method required for indexing the corpus
	TF-IDF model used for retrieval
	"""
	
	def __init__(self, filename):
		"""
		initialize several variables to use them throughout the program and for object instances
		"""
		self.filename = filename
		self.text = ""
		self.numPages = 0
		self.metadata = ""
		self.extract_from_pdf()

	def extract_from_pdf(self):
		with open(self.filename, 'rb') as pdf_file:
			pdf_reader = PyPDF2.PdfFileReader(pdf_file)
			self.numPages = pdf_reader.getNumPages()
			self.metadata = pdf_reader.documentInfo
			self.filename = self.metadata["/Title"]			

			for page_num in range(pdf_reader.numPages):
				pdf_page = pdf_reader.getPage(page_num)
				self.text += pdf_page.extractText()