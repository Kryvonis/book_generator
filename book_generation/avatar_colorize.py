from PIL import Image, ImageChops


def image_overlay(src_image, color):
    '''
    colorize gray image using overlay ps method
    :param src_image: image src, string to open file or PIL Image
    :param color: string in RGB 3 value separate by comma
    :return: colorize PIL Image
    '''
    if type(src_image) is str:
        src_image = Image.open(src_image)
    color = Image.new("RGBA", src_image.size, (*[int(x) for x in color.split(',')], 255))
    white = Image.new("RGBA", src_image.size, (0, 0, 0, 0))
    res_mul = ImageChops.multiply(src_image, color)
    res_scr = ImageChops.screen(res_mul, res_mul)
    res = Image.composite(res_scr, white, src_image)
    return res


def image_color(src_image, color):
    '''
        colorize gray image using color ps method
        :param src_image: image src, string to open file or PIL Image
        :param color: string in RGB 3 value separate by comma
        :return: colorize PIL Image
        '''
    if type(src_image) is str:
        src_image = Image.open(src_image)
    color = Image.new("RGBA", src_image.size, (*[int(x) for x in color.split(',')], 255))
    white_col = Image.new("RGBA", src_image.size, (0, 0, 0, 0))
    res = Image.blend(src_image, color, alpha=0.6)
    res = Image.composite(res, white_col, src_image)
    return res


def image_multiply(src_image, color):
    '''
        colorize gray image using multiply ps method
        :param src_image: image src, string to open file or PIL Image
        :param color: string in RGB 3 value separate by comma
        :return: colorize PIL Image
        '''
    if type(src_image) is str:
        src_image = Image.open(src_image)
    color = Image.new("RGBA", src_image.size, (*[int(x) for x in color.split(',')], 255))
    white_col = Image.new("RGBA", src_image.size, (0, 0, 0, 0))
    res = ImageChops.multiply(src_image, color)
    res = Image.composite(res, white_col, src_image)
    return res


def merge(first_img, second_img, position):
    '''
    paste one image to another using PIL
    :param first_img: image src, string to file or PIL Image would be background image
    :param second_img: image src, string to file or PIL Image would be in the top context
    :param position: coordinates tuple (x,y)
    :return: merging PIL image
    '''
    if type(first_img) is str:
        first_img = Image.open(first_img)
    if type(second_img) is str:
        second_img = Image.open(second_img)
    first_img.paste(second_img, position, second_img)
    return first_img
