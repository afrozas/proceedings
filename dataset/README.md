## Dataset
This is a dummy directory to preview the directory structure of the dataset. A sample processed json object is available [here](https://www.npoint.io/docs/cff3fbe85245376095a7).

> Download the dataset [here](https://drive.google.com/drive/folders/1vO1HH8KaaaYgd2dysTLMdviYsbtl7iM0?usp=sharing).

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
   |                  |            |            |
   | ---------------- | ---------- | ---------- |
   | `filename`       | `metadata` | `numPages` |
   | `title`          | `author`   | `subject`  |
   | `creator`        | `producer` | `keywords` |
   | `creationdate`   | `moddate`  | `trapped`  |
   | `ptexfullbanner` | `raw_text` | -          |
