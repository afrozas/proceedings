import os, json
from helpers.file_manager import FileManager
from helpers.pre_processor import Preprocessor
from tqdm import tqdm

def extract():
	"""
	"""

	# Get the list of all files to be indexed
	fm = FileManager("/media/enigmaeth/My Passport/eniext/code/experimental/proceedings/data/raw/papers.nips.cc")
	# fm = FileManager("/media/enigmaeth/My Passport/eniext/code/experimental/proceedings/data/test")
	files, fileNum = fm.get_files_to_be_indexed(), 0
	print("Getting files to be indexed...")
	print(f'Found {len(files)} files.')
	fails = []
	text_skips = []

	for file in tqdm(files):
		try:
			processedText = Preprocessor(file)
			filename = processedText.filename + '.json'
			filepath = str(os.path.join(fm.write_dir, filename))
			if len(processedText.sentences) == 0: text_skips.append(file)
			with open(filepath, 'w', encoding='utf-8') as f:
				json.dump(processedText.__dict__, f, ensure_ascii=False, indent=4)
		except:
			fails.append(file)

	succeed = [f for f in files if f not in (fails + text_skips)]
	
	print(f'Total: {len(files)}, Success: {len(succeed)}, Skipped: {len(text_skips)}, Failed: {len(fails)}')
	log = {
		"sucess": succeed,
		"text_skip": text_skips,
		"fail": fails,
	}
	log_filepath = str(os.path.join(fm.log_dir, "process_log.json"))
	with open(log_filepath, 'w', encoding='utf-8') as f:
			json.dump(log, f, ensure_ascii=False, indent=4)
	print("Processing logged.")

if __name__ == '__main__':
	extract()