import pyttsx3
import PyPDF2

book = open('ok.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)  # Updated to PdfReader
num_pages = len(pdfReader.pages)  # Changed from pdfReader.numPages
print(num_pages)

speaker = pyttsx3.init()
speaker.say('Hello Guys, I am Python audible')

for num in range(num_pages):
    page = pdfReader.pages[num]  # Access pages using .pages
    text = page.extract_text()
    speaker.say(text)

speaker.say('Thank you guys for listening to me')
speaker.runAndWait()
