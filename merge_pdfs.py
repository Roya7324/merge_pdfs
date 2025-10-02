from pypdf import PdfReader,PdfWriter
def merge_pdfs(paths,output):
    writer = PdfWriter()
    for path in paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output,"wb") as f:
        writer.write(f)

        