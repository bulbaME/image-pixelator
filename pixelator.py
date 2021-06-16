import sys
from PIL import Image

def pixelator(image, intensity, reduceColors = False):
    size = image.size
    r = reduceColors * 255 / 2

    for x in range(size[0]):
        for y in range(size[1]):
            # skip some pixels 
            xOff = x % intensity
            yOff = y % intensity
            
            pixel = image.getpixel((x - xOff, y - yOff))

            if r and not (xOff or yOff):
                newPixel = [0, 0, 0]
                for c in range(3):
                    color = int(pixel[c] / r)
                    newPixel[c] = int(color * r)
                pixel = tuple(newPixel)

            image.putpixel((x, y), pixel)
    image.save('pixelated.png')

if __name__ == '__main__':
    try:
        path, i, r = sys.argv[1:4]
        pixelator(Image.open(path), int(i), float(r))
    except:
        print('invalid input')