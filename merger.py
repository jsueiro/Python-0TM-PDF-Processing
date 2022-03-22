import sys
import PyPDF2

inputs = sys.argv[1:]  # grab all args


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write('super.pdf')


pdf_combiner(inputs)
