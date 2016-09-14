import pdfkit
page_options = {
    'page-height': '221',
    'page-width': '551',
    'margin-top': '3',
    'margin-right': '3',
    'margin-bottom': '3',
    'margin-left': '3',
    'dpi': '350',
}

cover_options = {
    'page-height': '221',
    'page-width': '551',
    'margin-top': '3',
    'margin-right': '3',
    'margin-bottom': '3',
    'margin-left': '3',
    'dpi': '350',
}

def create_page(src,out,options=page_options):
    f = open(src,'r')
    pdfkit.from_file(f, out, options=options)
    f.close()

