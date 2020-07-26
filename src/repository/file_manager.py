import os
from os import path


class FileManager:
	"""
	This class provides functions related to file management required for the indexer
	"""

	def __init__(self, root, accepted_formats, max_size):
		"""
		initialize variables: root path and accepted formats for the indexer
		"""
		self.root = root
		self.accepted_formats = accepted_formats
		self.size = max_size  # size in bytes
		self.write_dir = self.root + '/_json'
		self.log_dir = self.root + '/_log'
		self.process_write_and_log_dirs()

	def process_write_and_log_dirs(self):
		if path.exists(self.write_dir):
			print(f'Output dir found. Processing...')
		else:
			print(f'Creating output dir...')
			os.mkdir(self.write_dir)
			print(f'Created output dir: {self.write_dir}')
		if path.exists(self.log_dir):
			print(f'Log dir found.')
		else:
			print(f'Creating log dir...')
			os.mkdir(self.log_dir)
			print(f'Created log dir: {self.log_dir}')

	def get_all_files(self):
		"""
		List all files recursively in the root specified by root
		"""
		files_list = []
		for dirname, dirnames, filenames in os.walk(self.root):

			for filename in filenames:
				files_list.append(os.path.join(dirname, filename))

			if '.git' in dirnames:
				# don't go into any .git directories.
				dirnames.remove('.git')
		return files_list

	def get_files_to_be_indexed(self):
		"""
		returns list of files to be included in the index
		set `root` variable to the desired root
		:return: list of files to be indexed
		"""
		files = self.get_all_files()
		files_list = []
		for name in files:
			# process only accepted formats and files that are smaller than self.size bytes
			if name.split('.')[-1] in self.accepted_formats and os.stat(os.path.join(self.root, name)).st_size < self.size:
				files_list.append(os.path.join(self.root, name))
		return files_list
