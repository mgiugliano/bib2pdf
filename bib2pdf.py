#!/usr/local/bin/python3

# bib2pdf.py
#
# Mar 24th 2021 - (c) Michele Giugliano

import os
import sys
import bibtexparser

if len(sys.argv)<3:
    print ("USAGE: bib2pdf.py bibtexfile.bib path_for_files_download")
    exit()

pathdwn = sys.argv[2]

f= open("doi_list.txt","w")


bibfilename = str(sys.argv[1])


with open(bibfilename) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

N = len(bib_database.entries)

for i in range(N):
    #title = bib_database.entries[i]['title']
    doi   = bib_database.entries[i]['doi']
    if doi!='null':
        f.write(doi + '\n')

f.close()

os.system("/usr/local/bin/PyPaperBot --doi-file=""./doi_list.txt"" --dwn-dir=""" + pathdwn + """ --restrict=""1""")
#os.remove("bibtex.bib")
#os.remove("results.csv")
#os.remove("doi_list.txt")
