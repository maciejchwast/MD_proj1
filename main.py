from PIL import Image


def brighten(image):
    height = image.height
    width = image.width
    result = image

    value_brighten = input('Podaj wartosc z zakresu -255 - 255 o ktora obraz zostanie pojasniony lub sciemniony: ')

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y)) + int(value_brighten)
            result.putpixel((x, y), pixel)

    result.save('output_brighten.bmp')


def binarize(image):
    height = image.height
    width = image.width
    result = image

    value_binarize = input('Podaj wartosc graniczna binaryzacji: ')
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel < int(value_binarize):
                result.putpixel((x, y), 0)
            else:
                result.putpixel((x, y), 255)

    result.save('output_binarize.bmp')


'''
            |         |
    pixel11 | pixel12 | pixel 13
            |         |
    ----------------------------
            |         |
    pixel21 | pixel22 | pixel 33
            |         |
    ----------------------------
            |         |
    pixel31 | pixel32 | pixel 33
            |         |
'''


def filter(image, filter_type):
    filter_types = {'low_pass': [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]],
                    'high_pass': [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]],
                    'gauss': [[0.625, 0.125, 0.625], [0.125, 0.25, 0.125], [0.625, 0.125, 0.625]]}
    if filter_type not in filter_types:
        raise TypeError('Wrong filter type!')
    if filter_type == 'gauss':
        divider = 3
    else:
        divider = 1

    height = image.height
    width = image.width
    result = image
    weight = filter_types[filter_type]

    for x in range(width):
        for y in range(height):
            result.putpixel((x, y), int(get_3x3_pixel_array_and_sum_with_weight(image, x, y, weight)/divider))

    result.save(f'output_{filter_type}.bmp')


def get_3x3_pixel_array_and_sum_with_weight(image, x, y, weight_matrix):
    retval = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                to_add = image.getpixel((x+i, y+j))*weight_matrix[i+1][j+1]
            except:
                to_add = 0
            retval += to_add
    return retval


if __name__ == '__main__':
    #path_original_img = "Mapa_MD_no_terrain_low_res_Gray.bmp"
    #img = Image.open(path_original_img)
    #brighten(img)
    #binarize(img)

    path_binary = "Mapa_MD_no_terrain_low_res_Gray.bmp"
    img_bin = Image.open(path_binary)
    filter(img_bin, 'gauss')


