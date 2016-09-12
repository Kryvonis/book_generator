import pdfkit
options = {
    'page-height': '221',
    'page-width': '551',
    'margin-top': '3',
    'margin-right': '3',
    'margin-bottom': '3',
    'margin-left': '3',
    'dpi': '350',
}

def create_page(src,out):
    f = open(src,'r')
    pdfkit.from_file(f, out, options=options)
    # pdfkit.from_url('http://localhost:63342/Book_Creator/1.html?_ijt=669mj5r322c60tb62t2fno3fhn', out, options=options)
    # pdfkit.from_string(f, out, options=options)
    f.close()

