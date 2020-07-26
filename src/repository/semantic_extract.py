import os
import nltk.data
import spacy

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
nlp = spacy.load("en_core_web_sm")

class SemanticExtract:
	"""
	"""
	def __init__(self):
		"""
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
		for doc in nlp.pipe(texts):
			spacy_data["entities"] += [(ent.text, ent.label_)
									   for ent in doc.ents]
			spacy_data["tags"] += [(item.text, item.tag_) for item in doc]
			spacy_data["parser"] += [(item.text, item.head.text, item.dep_)
									 for item in doc]
			spacy_data["noun_chunks"] = [item.text for item in doc.noun_chunks]
		spacy_data["noun_chunks"] = list(set(spacy_data["noun_chunks"]))
		return spacy_data
