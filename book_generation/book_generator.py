class BookGenerator:
    def __init__(self, book_config):
        '''
        Class that describe proces of creation book
        :param book_config: all config for all book like - cover_type, avatar_config, text_on_pages
        '''
        self._book_config = book_config

    def give_book(self):
        '''
        generate pdf book using embedded functions
        for i in range(page_numbers):
            1.avatar_generator page 1
            2.paster_in_svg page 1
            3.avater_generator page 2
            4.paster_in_svg page 2
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
        hair_color = self._book_config.a_hair_color
        eye_color = self._book_config.a_eye
        skin_color = self._book_config.a_skin

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
