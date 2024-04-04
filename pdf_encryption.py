import pikepdf

old_pdf = pikepdf.Pdf.open("python.pdf")

no_extr = pikepdf.Permissions(extract = False)

old_pdf.save("pdf_encrypted.pdf", encryption = pikepdf.Encryption(user = "12345678", owner = "Akshay", allow = no_extr))