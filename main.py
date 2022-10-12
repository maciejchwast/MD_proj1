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


if __name__ == '__main__':
    path = "Mapa_MD_no_terrain_low_res_Gray.bmp"
    image = Image.open(path)
    brighten(image)
    binarize(image)



