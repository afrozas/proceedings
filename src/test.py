import os, json
from helpers.file_manager import FileManager
from helpers.format_converter import FormatConverter
from helpers.pre_processor import Preprocessor


def pre_process_and_query():
	"""
	Indexes the corpus using tf-idf vectorization
	Query pre-processed and documents returned on the basis of similarity
	"""

	# Get the list of all files to be indexed
	print("Getting files to be indexed")
	fm = FileManager("/media/enigmaeth/My Passport/eniext/code/experimental/proceedings/data/test")
	files, fileNum = fm.get_files_to_be_indexed(), 0
	for f in files:
		print(f, end="\n")
	print(len(files))

	extractedText = []

	# TF-IDF of each file and vectorization in file list to be indexed
	for file in files:
		print(fileNum, file)
		pdfText = Preprocessor(file)
		extractedText.append(pdfText)
		fileNum += 1 

	for text in extractedText:
		filename = text.filename.split('/')[-1] + '.json'
		with open(filename, 'w', encoding='utf-8') as f:
			json.dump(text.__dict__, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
	pre_process_and_query()