import os, subprocess
from helpers.file_manager import FileManager


class FormatConverter:
	"""
	textract does not support text extraction from files of .ppt format
	this class provides converter methods for such formats
	"""
	def ppt_to_pdf():
		"""
		converts .ppt files to .pdf for easier text extraction
		"""
		fm = FileManager()
		files_list = fm.get_all_files()
		for file in files_list:
			if file.split('.')[-1] == 'ppt':
				command = "unoconv -f pdf " +  str(file.replace(" ", "\ "))
				try:
					subprocess.call(command, shell=True)
					print("converted :: ", str(file))
				except:
					print("Error while converting ", str(file), " to PDF")