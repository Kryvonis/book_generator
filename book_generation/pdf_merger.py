from PyPDF2 import PdfFileReader,PdfFileWriter

# Creating a routine that appends files to the output file


# Creating an object where pdf pages are appended to


def merge_pdf(input_pdf,output_pdf):
    output = PdfFileWriter()
    # Appending two pdf-pages from two different files
    _input_pdf = PdfFileReader(open(input_pdf,"rb"))
    for i in range(30):
        output.addPage(_input_pdf.getPage(0))
    # output.addPage(_input_pdf.getPage(0))
    # output.addPage(_input_pdf.getPage(0))

    # Writing all the collected pages to a file
    output.write(open(output_pdf,"wb"))