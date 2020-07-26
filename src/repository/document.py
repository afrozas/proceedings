import string
import PyPDF2
import textract
import re
from repository.semantic_extract import SemanticExtract

class Document:
    """
    Document class provides method required for indexing the corpus
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
        self.semantic_extract()
        # Use document title as filename in final json
        self.filename = self.title + '.json'

    def semantic_extract(self):
        semantic_extract = SemanticExtract()
        self.sentences = semantic_extract.nltk_sent_extract(self.raw_text)
        self.process_spacy_data(
            semantic_extract.spacy_entity_extract(self.sentences))

    def process_spacy_data(self, spacy_data):
        for key in spacy_data:
            setattr(self, key, spacy_data[key])

    def extract_from_pdf(self):
        try:
            with open(self.filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                self.numPages = pdf_reader.getNumPages()
                for key in pdf_reader.documentInfo:
                    setattr(self, str(key.replace('/', '')).lower(),
                            pdf_reader.documentInfo[key])
                self.raw_text = self.extract_text(self.filename)

        except:
            pass
            print(f'Couldn\'t extract from {self.filename}')

    def extract_text(self, file):
        """
        Extract text from a file.
        :param file: expects file path as param to be processed by textract
                                                         textract extracts text from various file formats
        :return: text extracted from file in lower case
        """
        try:
            txt = textract.process(
                str(file),  encoding="utf-8", errors='ignore')  # returns byte text
            txt = txt.decode('utf-8')  # converts bytes to string
            # printing here leads to non-printable characters also being displayed
            # removes escape characters using regex
            txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', txt)
            # removes unicode characters like \u0097 and type(txt) is bytes
            txt = txt.encode('ascii', 'ignore')
            txt = txt.split()
            newTxt = []
            for text in txt:
                try:
                    newTxt.append(text.decode('unicode_escape'))
                except:
                    pass
            txt = ' '.join(newTxt)
        except:
            txt = ""
        return txt
