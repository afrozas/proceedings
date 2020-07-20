## Search Engine for Course Management Systems

Search engine built from scratch for searching resources( Powerpoint presentations, PDFs, Word documents, etc) for different courses on BITS Course Management System.

> This repo uses python3.5 as textract library is not available for python2.7 .
Install all the other dependencies using pip3.

### Installation:

Run the follwing in terminal.
```
$ sudo pip install -r requirements.txt
```
If you face any problem, install `textract` and `nltk` separately.

#### Installing `textract`

```
$ sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev

$ sudo pip3 install textract
```

#### Installing `nltk`

```
$ pip3 install nltk
$ python3
>>> import nltk
>>> nltk.download()
	[Press 'd' for download]
	Download() d

	Packages: all
```

#### How to Use

> Extensive Documentation on the classes, methods and variables used can be found inline as docstrings and comments.

** Please set the `root` variable(inside `test.py` file) to path of root of directory containing sub-directories and files to be indexed. ** 

Once inside the root of this directory, you can query using the following command.

```
$ python3 test.py 
```
This will start indexing and you will be prompted with a query field once all the files are indexed.

```
Enter query: 
```
Files are queried based on the input here. 

> Making sense of the results: 

		The following structure is maintained in the returned list of files.

		<file_rank_1> | <file_name_with_path> | <relevance_score>
		<file_rank_2> | <file_name_with_path> | <relevance_score>

**Relevance Score**

 The relevance score of each document is calculated based upon the TF-IDF frequency of the keywords and cosine similarity between the file and query vectors. 

To quit the program, **`quit()`** can be used.
```
Enter query : quit()
```

### Issues:
- In .doc files, pipes are being extracted from table borders.
- .ppt is not currently supported by textract, hence unoconv is to be used for .ppt files specifically
