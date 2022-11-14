from PIL import Image


def load_bmp():
    src = r'./white.jpg'
    img = Image.open(src)
    return img


def putFpixel(image):
    image.putpixel((300, 0), 0)

    return image


def zamiana(liczba):
    tablica = []
    for i in range(8):
        nowa = liczba % 2
        if nowa == 0:
            nowa = 255
        else:
            nowa = 0
        tablica.append(nowa)
        if (liczba % 2 == 0):
            liczba = liczba / 2
        else:
            liczba = (liczba - 1) / 2

    return tablica


def XRule(image, liczba):
    width = image.width
    height = image.height
    for j in range(0, height - 1):
        for i in range(0, width - 1):
            pixel = image.getpixel((i, j))[0]
            pixelP = image.getpixel((i - 1, j))[0]
            pixelN = image.getpixel((i + 1, j))[0]
            if pixelP == 0 and pixel == 0 and pixelN == 0:
                image.putpixel((i, j + 1), zamiana(liczba)[7])
            elif pixelP == 0 and pixel == 0 and pixelN == 255:
                image.putpixel((i, j + 1), zamiana(liczba)[6])
            elif pixelP == 0 and pixel == 255 and pixelN == 0:
                image.putpixel((i, j + 1), zamiana(liczba)[5])
            elif pixelP == 0 and pixel == 255 and pixelN == 255:
                image.putpixel((i, j + 1), zamiana(liczba)[4])
            elif pixelP == 255 and pixel == 0 and pixelN == 0:
                image.putpixel((i, j + 1), zamiana(liczba)[3])
            elif pixelP == 255 and pixel == 0 and pixelN == 255:
                image.putpixel((i, j + 1), zamiana(liczba)[2])
            elif pixelP == 255 and pixel == 255 and pixelN == 0:
                image.putpixel((i, j + 1), zamiana(liczba)[1])
            elif pixelP == 255 and pixel == 255 and pixelN == 255:
                image.putpixel((i, j + 1), zamiana(liczba)[0])

        ost = image.getpixel((i, j))
        if ost == 0:
            image.putpixel((1, j + 1), 0)

    image.show()


if __name__ == '__main__':
    imag = load_bmp()
    putFpixel(imag)
    XRule(putFpixel(imag), 90)
    print(zamiana(26))
