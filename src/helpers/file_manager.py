import os


class FileManager:
	"""
	This class provides functions related to file management required for the indexer
	"""

	def __init__(self, root):
		"""
		initialize variables: root path and accepted formats for the indexer
		"""
		self.root = root
		self.accepted_formats = ['pdf']


	def get_all_files(self):
		"""
		List all files recursively in the root specified by root
		"""
		files_list = []
		for dirname, dirnames, filenames in os.walk(self.root):

			# print path to all filenames.
			for filename in filenames:
				files_list.append(os.path.join(dirname, filename))
				print(os.path.join(dirname, filename))

			# Advanced usage:
			# editing the 'dirnames' list will stop os.walk() from recursing into there.
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
			if name.split('.')[-1] in self.accepted_formats:
				files_list.append(os.path.join(self.root, name))
		return files_list[0:-1]
