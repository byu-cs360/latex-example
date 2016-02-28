# LaTeX Example

Example code showing how to use the LaTeX to write a paper.

1) If you want to use pdflatex (and PNG figures) to produce the paper, run:

```
pdflatex paper
bibtex paper
pdflatex paper
pdflatex paper
```

This ensures the bibliography is included properly.  It will
produce a PDF output.

I have included a Makefile that will do this for you.

2) If you want to use latex (and EPS figures) to produce the paper, run:

```
latex paper
bibtex paper
latex paper
latex paper
```

This ensures the bibliography is included properly.  It will
produce a dvi output.

To generate postscript, do:

```
dvips -o paper.ps paper
```

To generate PDF, do:

```
dvips -Ppdf -G0 -o paper.ps paper
ps2pdf paper.ps
```

I have included a Makefile.latex that will do this for you.

3) The file apache-thread-mpm.svg is an SVG formatted figure, which I created
using inkscape.  I exported this to PNG format in inkscape and then
used Gimp to convert this to EPS.

4) The file tcp.py is a Python script to generate a figure using biggles.
You can run it with:

```
python tcp.py
```

and it will produce both a PNG and an EPS figure.

5) The file tcp.gnu is a gnuplot script to generate a figure using the
tcp.data file.  You can run it with:

```
gnuplot tcp.gnu
```

and it will produce either a PNG or an EPS figure.
