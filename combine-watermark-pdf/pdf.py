import PyPDF2
import sys

command = sys.argv[1]
pdf_list = sys.argv[2:]

pdf_file = sys.argv[2]
pdf_watermark = sys.argv[3]

# combine pdf
def combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("./sample-pdf/combine.pdf")


# watermark pdf
def watermarker(pdf, watermark):
    template = PyPDF2.PdfFileReader(open(pdf, "rb"))
    watermark = PyPDF2.PdfFileReader(open(watermark, "rb"))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open("./sample-pdf/watermarked_output.pdf", "wb") as file:
            output.write(file)


if command == "combine":
    combiner(pdf_list)
elif command == "watermarker":
    watermarker(pdf_file, pdf_watermark)