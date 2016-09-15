# from book_generation import avatar_colorize, pdf_creation, pdf_merger, svg_merge
# from book_generation import BookGenerator
# # bg = BookGenerator()
# import base64
# avatar_colorize.image_overlay('image_begin/1.png', '255,0,0').save('image_end/1.png')
# svg_merge.paste_elem('svg_tmp/1.svg', 'image_end/1.png')
#
# #
# # with open('fonts/Heartwell.otf', "rb") as image_file:
# #     encoded_string = str(base64.b64encode(image_file.read()))
# # print(encoded_string)
#
#
#
# # pdf_creation.create_page('svg_tmp/2.svg', 'pdf_end/1.pdf')
# pdf_creation.create_page('test.html', 'pdf_end/2.pdf')
# # pdf_creation.create_page('test.html', 'pdf_end/1.pdf')
# # pdf_merger.merge_pdf('pdf_end/1.pdf','pdf_end/res.pdf')
#
#
#
#
# #avatar 'image_begin/1.png'
# #color  '255,0,0'
# #svg_template 'svg_tmp/1.svg'
# #pdf_pages 'pdf_end/1.pdf'
# #pdf_result 'pdf_end/res.pdf'
#
#
# #######################
# #### FRONTEND INFO ####
# #######################
#
# # avatar_config
# # type of book
#
#
#
#
def couritine(f):
    def wrap(*args,**kwargs):
        gen = f(*args,**kwargs)
        gen.send(None)
        return gen
    return wrap

@couritine
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)

c = calc()

print(type(c)) # <type 'generator'>

# c.next() # Необходимая инициация. Можно написать c.send(None)
# c.send(None) # Выведет 3
c.send((1,2)) # Выведет 3
c.send((100, 30)) # Выведет 130
c.send((100, 30)) # Выведет 130
c.send((100, 30)) # Выведет 130
c.send((100, 30)) # Выведет 130
# c.send((666, 0)) # Выведет 666
c.send(('h',0)) # Выведет [3, 130, 666]
# c.close() # Закрывем генератор