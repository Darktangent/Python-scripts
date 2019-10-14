import PyPDF2
# import sys

# inputs = sys.argv[1:]
template = PyPDF2.PdfFileReader(open('twopage.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open("watermarked_output.pdf", 'wb') as file:
        output.write(file)

# def water_mark(pdf_list):
#     writer = PyPDF2.PdfFileWriter()
#     for pdf in pdf_list:
#         print(pdf)


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#         merger.write('super.pdf')


# pdf_combiner(inputs)


# with open('./dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
