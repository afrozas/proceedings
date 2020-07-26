import os
import json
from repository.file_manager import FileManager
from repository.document import Document
from tqdm import tqdm
import argparse


def process_directory(args):
	"""
	Process all files in a directory.
	Creates _json with one json per processed file.
	Creates _log with stats and details on processing.
	"""
	accepted_formats = ["pdf"]
	max_size = 5 * 1000000
	if not args.directory:
		raise AssertionError("No directory found. Please specify a directory. python extract.py --directory <dir_name>")
	if args.accepted_formats:
		accepted_formats = args.accepted_formats
	if args.max_size:
		max_size = args.max_size

	# Get the list of all files to be indexed
	fm = FileManager(args.directory, accepted_formats, max_size)
	files, fileNum = fm.get_files_to_be_indexed(), 0
	print("Getting files to be indexed...")
	print(f'Found {len(files)} files. Processing...')

	failure = []
	text_skip = []
	for file in tqdm(files):
		try:
			processedText = Document(file)
			filename = processedText.filename + '.json'
			filepath = str(os.path.join(fm.write_dir, filename))
			if len(processedText.sentences) == 0:
				text_skip.append(file)
			with open(filepath, 'w', encoding='utf-8') as f:
				json.dump(processedText.__dict__, f,
						  ensure_ascii=False, indent=4)
		except:
			failure.append(file)

	success = [f for f in files if f not in (failure + text_skip)]

	print(
		f'Total: {len(files)}, Success: {len(success)}, Skips: {len(text_skip)}, Failures: {len(failure)}')
	log = {
		"stats": {
			"success": len(success),
			"text_skip": len(text_skip),
			"failure": len(failure),
		},
		"files": {
			"sucess": success,
			"text_skip": text_skip,
			"failure": failure,
		}
	}
	log_filepath = str(os.path.join(fm.log_dir, "process_log.json"))
	with open(log_filepath, 'w', encoding='utf-8') as f:
		json.dump(log, f, ensure_ascii=False, indent=4)
	print("Processing logged.")


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--directory", help="Root dir with documents to process. eg: ~/docs/acl/acl_2015")
	parser.add_argument("--accepted_formats", help="File extensions to process. Default: [\"pdf\"]")
	parser.add_argument("--max_size", help="Max size of a single file to process. Default: 5MB")
	args = parser.parse_args()
	process_directory(args)
