import glob
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
 
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        try:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
        except:
            pass
        
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)
 
 
if __name__ == '__main__':
    paths = ["img//cover.pdf",
            "Fundamentos del lenguaje.pdf",
            "Matplotlib, visualización gráfica.pdf",
             "Sympy, un sistema de álgebra computacional.pdf"
            ]
    print(glob.glob("*.pdf"))
    
    # ~ os.remove("python_notes.pdf")
    merger('python_notes.pdf', paths)
