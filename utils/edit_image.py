from config import get_notes
from PIL import Image, ImageEnhance


path = "/Users/dnv/Downloads/img_from_html"


def enhance_image(img_path: str):
    # read the image
    im = Image.open(img_path)

    # enhance contrast
    im = ImageEnhance.Contrast(im).enhance(factor=2.5)

    # enhance brightness
    im = ImageEnhance.Brightness(im).enhance(factor=0.97)

    # enhance sharpness
    im = ImageEnhance.Sharpness(im).enhance(factor=3)

    # rotate and save
    im.rotate(angle=270, expand=True).save(img_path)


if __name__ == '__main__':
    notes = get_notes(path=path, suffix=".jpg")
    for note in notes:
        enhance_image(f"{path}/{note}")




