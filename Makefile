# Makefile for the paper using pdflatex

MAIN := $(patsubst %.tex,%.pdf,$(wildcard *.tex))

%.pdf : %.tex
	pdflatex $<
	bibtex $(<:%.tex=%)
	pdflatex $<
	pdflatex $<

all: $(MAIN)
	rm -f *.aux *.log

clean:
	rm -f *.aux *.log *.dvi *.blg *.bbl

realclean:
	rm -f *.aux *.log *.dvi *.blg *.bbl *.ps *.pdf

# If you want your files automatically updated whenever an included figure
# changes, then you have to manually add the dependencies here.  At some
# future point I will figure out how to do this automatically.

paper.pdf: apache-thread-mpm.png tcp.png

.PHONY: all

