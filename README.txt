How to use these scripts:

---------------

NOTE: Unless otherwise specified, all scripts require Python 2.7 and NLTK v3 (py27-nltk on Macports), and must be run in the same directory as the target transcript document.

---------------

NCC.PY

Function: Gets a concordance, or a list, of a target word as it shows up in the transcript with the target word in the middle surrounded by 25 characters of context on either side of each instance.

How to use: Run in the command line as follows.
$ python2.7 ncc.py fname textword

(fname = file name, such as transcript.txt)
(textword = the target word to get a concordance for)

---------------

NCL.PY

Function: Gets a list of possible collocations, or words that show up together frequently in the text and may be related as a phrase.

How to use: Run in the command line as follows.
$ python2.7 ncl.py fname

(fname = file name, such as transcript.txt)