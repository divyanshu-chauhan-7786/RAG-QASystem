from QAWithPDF.web_loader import load_website

docs = load_website("https://en.wikipedia.org/wiki/Artificial_intelligence")
print(len(docs))
print(docs[0].text[:500])
