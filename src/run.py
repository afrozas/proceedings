import os, json
from helpers.file_manager import FileManager
from helpers.format_converter import FormatConverter
from helpers.pre_processor import Preprocessor


def extract():
	"""
	"""

	# Get the list of all files to be indexed
	print("Getting files to be indexed")
	fm = FileManager("/media/enigmaeth/My Passport/eniext/code/experimental/proceedings/data/test")
	files, fileNum = fm.get_files_to_be_indexed(), 0
	for f in files:
		print(f, end="\n")
	print(len(files))

	extractedText = []

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
	extract()