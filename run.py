from book_generation import avatar_colorize, pdf_creation, pdf_merger, svg_merge
from book_generation import BookGenerator
# bg = BookGenerator()
import base64
# import os,inspect

# print(os.path.abspath('image_end/1.png'))


avatar_colorize.image_overlay('image_begin/1.png', '255,0,0').save('image_end/1.png')
svg_merge.paste_elem('svg_tmp/1.svg', 'image_end/1.png')
pdf_creation.create_page('svg_tmp/3.svg', 'pdf_end/1.pdf')
# pdf_merger.merge_pdf('pdf_end/1.pdf','pdf_end/res.pdf')


#avatar 'image_begin/1.png'
#color  '255,0,0'
#svg_template 'svg_tmp/1.svg'
#pdf_pages 'pdf_end/1.pdf'
#pdf_result 'pdf_end/res.pdf'

#######################
#### FRONTEND INFO ####
#######################

# avatar_config
# type of book
import subprocess

