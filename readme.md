# bib2pdf

This (python) command-line utility parses a bibtex file, provided as input, and
attempts at downloading all the PDF files corresponding to the entries.

It employs two Python libraries:
- Python-BibTexParser (https://github.com/sciunto-org/python-bibtexparser)
- PyPaperBot (https://github.com/ferru97/PyPaperBot)

The former allows parsing the BibTex file and navigating its entries, extracting
the DOI or other information relevant to identify the article.

Install:
/usr/local/bin/pip3 install PyPaperBot
/usr/local/bin/pip3 install bibtexparser
