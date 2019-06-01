@ECHO OFF
REM pdflatex python-apuntes.tex
pdflatex -interaction=nonstopmode python-apuntes.tex
bibtex python-apuntes
pdflatex -interaction=nonstopmode python-apuntes.tex
python-apuntes.pdf
exit