pdflatex -synctex=1 -interaction=nonstopmode "Pflichtenheft.tex" 
makeindex -s nomencl.ist -o Pflichtenheft.nls Pflichtenheft.nlo
pdflatex -synctex=1 -interaction=nonstopmode "Pflichtenheft.tex" 