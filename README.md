# Proceedings

Metadata, text and semantic extraction of conference proceedings to build knowledge graph and semantic search engines.

## Dataset

The dataset covers major conferences in machine learning, natural language and speech processing.

### Data

The current release of the dataset has documents processed from the
following conference proceedings.

| NeurIPS | EMNLP |  ACL  | InterSpeech |
| :-----: | :---: | :---: | :---------: |
|    -    |   -   |   -   |      -      |
|  2019   | 2019  | 2019  |    2019     |
|  2018   |   -   | 2018  |    2018     |
|  2017   |   -   | 2017  |    2017     |
|  2016   |   -   | 2016  |      -      |
|  2015   |   -   | 2015  |      -      |

> Note: Few files from certain proceedings are dropped from the dataset due to parsing errors.

### Features

 The dataset contains the following fields extracted from each document.

- Semantically extracted fields using a [nltk](https://www.nltk.org/) and [spacy](https://spacy.io/) pipeline.
  - [`entities`](https://spacy.io/usage/linguistic-features#named-entities): Named Entity Recognition is performed on the document text to extract text span as entites and tag them with entity_type.
  - [`tags`](https://spacy.io/usage/linguistic-features#pos-tagging): Part of Speech tagged tokens extracted from document text.
  - [`parser`](https://spacy.io/usage/linguistic-features#dependency-parse): Dependency Parsing between text spans of document.
  - [`noun_chunks`](https://spacy.io/usage/linguistic-features#noun-chunks): Base noun phrases that have a noun as their head.
- Metadata fields extracted using PyPDF2
  - `filename`,
  - `text`,
  - `numPages`,
  - `metadata`,
  - `title`,
  - `author`,
  - `subject`,
  - `creator`,
  - `producer`,
  - `keywords`,
  - `creationdate`,
  - `moddate`,
  - `trapped`,
  - `ptexfullbanner`,
  - `raw_text`

## Local Development

An instance of the extraction pipeline can be run locally to produce processed json in the same format as the dataset.

### Installation

Clone the repository and cd into `proceedings/`.

```bash
git clone https://github.com/enigmaeth/proceedings
cd proceedings/
```

The repository requires `python3` to be installed. Check the python version and initialise a virtualenv to install requirements.

```bash
$ python --version
Python 3.6.9

$ python3 -m venv .
$ source .env/bin/activate
$ pip install -r requirements.txt
```

Download the required spacy and nltk modules.

```bash
$ pip install -U spacy
$ pip install -U spacy-lookups-data
$ python -m spacy download en_core_web_sm

# Install the nltk punkt module
$ python3
>>> import nltk
>>> nltk.download()
NLTK Downloader
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> punkt

# punkt module should be downloaded now.
```

## Using `extract.py`

The entry point for the pipeline is [`src/extract.py`](src/extract.py). It defines the following three arguments.

```markdown
  --directory DIRECTORY **REQUIRED**
                        Root dir with documents to process.
                        eg: ~/docs/acl/acl_2015
  --accepted_formats ACCEPTED_FORMATS
                        File extensions to process. Default: ["pdf"]
  --max_size MAX_SIZE   Max size of a single file to process. Default: 5MB
```

To process a documents directory with `extract.py`, run the following command:

```bash
python3 extract.py --directory <path/to/directory>
```

## Contributing

### Add a new proceeding

Contributions for adding processed proceedings are welcome and would help grow the dataset quickly.

- If you are interested in adding a new proceeding, please follow the steps in [`Local Development`](README.md#Local_Development) and send a Pull Request!

- If you want a new proceeding to be added, please open a new issue using the template here!

### Adding a new semantic extraction component

All the semantic extraction components live inside [`src/repository/semantic_extract.py`](src/repository/semantic_extract.py) file.

- If you are interested in adding a new semantic extraction component, please follow the steps in [`Local Development`](README.md#Local_Development) to run a local instance. Verify if your component works by running it on the [`test`](test/) directory and send a Pull Request!

- If you want a new component to be added, please open a new issue using the template here!

## LICENSE

The project is licensed under a Creative Commons Attribution-NonCommercial 4.0 International [License](/LICENSE).
