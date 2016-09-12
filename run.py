import avatar_colorize as ac
import svg_merge as sm
import pdf_creation
ac.image_overlay('image_begin/1.png','255,0,0').save('image_end/1.png')
sm.swap_elem('svg_tmp/1.svg','image_end/1.png')
# pdf_creation.create_page('svg_tmp/2.svg','pdf_end/1.pdf')
# pdf_creation.create_page('svg_tmp/envelope_coaster.svg','pdf_end/1.pdf')
pdf_creation.create_page('1.html','pdf_end/1.pdf')
# pdf_creation.create_page('svg_tmp/perspective.svg','pdf_end/1.pdf')