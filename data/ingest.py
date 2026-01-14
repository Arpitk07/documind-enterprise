from pypdf import PdfReader

reader = PdfReader("sample1.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()