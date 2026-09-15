from docxpy import DOCReader

FILE = "./DixRes.docx"

def extract_text():
    docx = DOCReader(FILE)
    
    text = docx.process()

    return text
    


    