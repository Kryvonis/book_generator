import book_generation.avatar_colorize


class BookGenerator:
    def __init__(self, book_config,
                 page_options=None, cover_options=None):
        '''
        Class that describe proces of creation book. Need to test all book_config.
        :param book_config: all config for all book like - cover_type, avatar_config, text_on_pages
        '''
        self.__book_config = book_config
        if page_options:
            self.__page_options = page_options
        else:
            self.__page_options = {
                'page-height': '221',
                'page-width': '551',
                'margin-top': '3',
                'margin-right': '3',
                'margin-bottom': '3',
                'margin-left': '3',
                'dpi': '350',
            }
        if cover_options:
            self.__cover_options = cover_options
        else:
            self.__cover_options = {
                'page-height': '221',
                'page-width': '551',
                'margin-top': '3',
                'margin-right': '3',
                'margin-bottom': '3',
                'margin-left': '3',
                'dpi': '350',
            }

    def give_book(self):
        '''
        Process can take more time. Need to run async

        generate pdf book using embedded functions
        for i in range(1,page_numbers,2):
            1.avatar_generator page i
            2.paster_in_svg page i
            3.avater_generator page i+1
            4.paster_in_svg page i+1
            5.merger_svg
            6.generate_pdf_page
        7.merger_page_pdf

        :return: two url for cover_pdf and book_pdf
        '''
        pass

    def __avatar_generator(self):
        '''
        colorize and merge avatar for one page and save in some file
        :return: url for generated file in png
        '''
        hair_color = self.__book_config.a_hair_color
        eye_color = self.__book_config.a_eye
        skin_color = self.__book_config.a_skin

    def __paster_in_svg(self):
        '''
        get all requirements and insert in one page in svg.
        photos paste in base64
        delete all files after insertion
        :return: url for generated file in svg
        '''
        pass

    def __merger_svg(self):
        '''
        use to merge two svg's in one book reversal
        :return: url for generated file in svg
        '''
        pass

    def __generate_page_pdf(self):
        '''
        use generated pdf to create one page in pdf format
        :return: url for generated file in pdf
        '''
        pass

    def __merger_page_pdf(self):
        '''
        use to merge all pdf pages in one book
        delete all files after merging
        :return: url for generated file in pdf
        '''
        pass
