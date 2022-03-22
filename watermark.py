import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):  # return numpages
    page = template.getPage(i)  # obtengo cada pag
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermark_output.pdf', 'wb') as file:
        output.write(file)
