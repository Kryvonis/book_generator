import pdfkit


page_options = {
    'page-height': '221',
    'page-width': '551',
    'margin-top': '3',
    'margin-right': '3',
    'margin-bottom': '3',
    'margin-left': '3',
    'dpi': '350',
    'user-style-sheet': 'st.css',
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
    # f = open(src)
    with open(src,'r') as f:
        print(pdfkit.from_file(f, out, options=options))
    # pdfkit.from_file(f, out)
    # f.close()

