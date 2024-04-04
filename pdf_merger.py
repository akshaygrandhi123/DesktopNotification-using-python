from glob import glob
from pikepdf import Pdf

new_pdf = Pdf.new()

for file in glob("*.pdf"):
    olf_pdf = Pdf.open(file)
    new_pdf.pages.extend(olf_pdf.pages)
new_pdf.save("demo.pdf")