import pdfkit

options = {
    'page-height': '221',
    'page-width': '551',
    'margin-top': '3',
    'margin-right': '3',
    'margin-bottom': '3',
    'margin-left': '3',
    'encoding': "UTF-8",
    'dpi': '350',
}

def create_page(src,out):
    with open(src) as f:
        pdfkit.from_file(f, out, options=options)
