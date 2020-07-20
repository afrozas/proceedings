from helpers.pre_processor import Preprocessor
from nltk.corpus import stopwords


class Query:
	"""
	Query class provides method required for preprocessing the query and calculating the results
	"""

	def __init__(self):
		"""
		initialize several variables to use them throughout the program and for object instances
		"""
		self.preprocessor = Preprocessor()
		self.keywords = ""
		self.results = []


	def query_preprocess(self):
		"""
		method to preprocess the query
		tokenizes, stems unigrams, generate list of keywords including bigrams and trigrams
		saves the above generated keywords to self.keywords
		"""
		self.input = input("Enter query: ")
		print(self.input)
		tokens = self.preprocessor.tokenize(self.input)
		ngrams = self.preprocessor.generate_ngrams(tokens)
		ngrams[0] = self.preprocessor.stem(ngrams[0])
		self.keywords = ngrams[0] + ngrams[1] + ngrams[2]
		self.keywords = [word for word in self.keywords if word not in self.preprocessor.stopwords]
			

	def display_results(self, numFiles):
		"""
		method to calculate the similarity for documents and return results
		:Calculates similarity based on cosine product of query vector and documents vectors
		:Assigns similarity scores to the products, results sorted by score
		:param numFiles: total number of files in the corpus
		:return:
		"""
		self.results = []
		for fileNum in range(numFiles):
			score = 0.0
			for keyword in self.keywords:
				if keyword in self.preprocessor.TF_IDF_Vector and fileNum in self.preprocessor.TF_IDF_Vector[keyword]:
					score += self.preprocessor.TF_IDF_Vector[keyword][fileNum]
			self.results.append((score,fileNum)) #/self.preprocessor.docLength[fileNum]
		self.results.sort()