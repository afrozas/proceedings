import string, os, math
import PyPDF2
import textract, re
import string, os, math
import PyPDF2
import nltk.data
import spacy

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
nlp = spacy.load("en_core_web_sm")
# nlp.add_pipe(nlp.create_pipe('textcat'), after='tagger')

class SemanticExtract:
	"""
	Preprocessor class provides method required for indexing the corpus
	TF-IDF model used for retrieval
	"""
	
	def __init__(self, processedPdf):
		"""
		initialize several variables to use them throughout the program and for object instances
		"""
		pass

	def nltk_sent_extract(self, text):
		return tokenizer.tokenize(text)

	def spacy_entity_extract(self, texts):
		spacy_data = {
			"entities": [],
			"tags": [],
			"parser": [],
			"noun_chunks": [],
		}
		# print(nlp.pipeline)
		for doc in nlp.pipe(texts):
			spacy_data["entities"] += [(ent.text, ent.label_) for ent in doc.ents]
			spacy_data["tags"] += [(item.text, item.tag_) for item in doc]
			spacy_data["parser"] += [(item.text, item.head.text, item.dep_) for item in doc]
			spacy_data["noun_chunks"] = [item.text for item in doc.noun_chunks]
		spacy_data["noun_chunks"] = list(set(spacy_data["noun_chunks"]))
		return spacy_data

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
		self.title = ""
		self.extract_from_pdf()
		semantic_extract = SemanticExtract(self)
		self.sentences = semantic_extract.nltk_sent_extract(self.raw_text)
		self.process_spacy_data(semantic_extract.spacy_entity_extract(self.sentences))
		self.filename = self.title

	def process_spacy_data(self, spacy_data):
		for key in spacy_data:
			setattr(self, key, spacy_data[key])

	def extract_from_pdf(self):
		try:
			with open(self.filename, 'rb') as pdf_file:
				pdf_reader = PyPDF2.PdfFileReader(pdf_file)
				self.numPages = pdf_reader.getNumPages()
				for key in pdf_reader.documentInfo:
					setattr(self, str(key[1:]).lower(), pdf_reader.documentInfo[key])
				self.raw_text = self.extract_text(self.filename)
		
		except:
			pass
			print(f'Couldn\'t extract from {self.filename}')

	def extract_text(self, file):
		"""
		extract text from a file
		file can be of different formats : .pptx, .pdf, .docx
		:param file: expects file path as param to be processed by textract
					 textract extracts text from various file formats
		:return: text extracted from file in lower case
		"""
		try:
			txt = textract.process(str(file),  method='pdfminer', encoding="utf-8", errors='ignore') # returns byte text
			txt = txt.decode('utf-8') # converts bytes to string
							# printing here leads to non-printable characters also being displayed
			txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
			txt = txt.encode('ascii','ignore') # removes unicode characters like \u0097 and type(txt) is bytes
			txt = txt.split()
			newTxt = []
			for text in txt:
				try:
					newTxt.append(text.decode('unicode_escape')) # conversion to desired string 
				except:
					pass
			txt = ' '.join(newTxt)	
		except:
			txt = ""
		return txt