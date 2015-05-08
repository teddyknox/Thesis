#!/bin/bash
set -e
pdflatex thesis.tex
bibtex thesis.aux
pdflatex thesis.tex
pdflatex thesis.tex
open thesis.pdf
