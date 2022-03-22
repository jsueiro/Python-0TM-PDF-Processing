import PyPDF2

with open('dummy.pdf', 'rb') as file:  # convert to binary mode read
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    # print(reader.getPage(0))  # devuelve page object

    # rotar pagina
    page = reader.getPage(0)
    page.rotateClockwise(180)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
