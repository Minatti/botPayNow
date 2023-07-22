from PyPDF2 import PdfReader

path = "C:/users/workcarminatti/Downloads/arquivo.pdf"
print(path)

reader = PdfReader(path)
page = reader.pages[0]
text = page.extract_text()
rows = text.split("\n")


for i in rows:
    k = i.split(",")
    print(k)
 

    
