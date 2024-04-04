#PDF Editor - Does replacing pages, deleting pages, reversing pages

import pikepdf

old_pdf = pikepdf.Pdf.open("python.pdf")

# Replacing Pages:
# old_pdf.pages[4]=old_pdf.pages[0]
# old_pdf.save("rep_new.pdf")

# Deleting Pages:
# del old_pdf.pages[1:3]
# old_pdf.save("del_new.pdf")

# Reversing Pages:
# old_pdf.pages.reverse()
# old_pdf.save("rev_new.pdf")

# Extracting Pages:
# old_pdf.pages.extend(old_pdf.pages[1:3])  
# old_pdf.save("ext_new.pdf")
