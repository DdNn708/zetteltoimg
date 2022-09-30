import imgkit

from config import ZETTELS_LIST, ZETTELKASTENDIR, SUBDIR, IMGDIR, OPTIONS, gen_html_view
from utils.zettel import Zettel


def transform_zettel_to_image():
    for filename in ZETTELS_LIST:
        # create zettel and set parameters
        zettel = Zettel()
        zettel.set_name(filename)
        zettel.set_path_v2(f'{ZETTELKASTENDIR}{SUBDIR}')
        zettel.set_html_content()

        # generate img
        html = gen_html_view(zettel.name, zettel.content)
        imgdir = IMGDIR + zettel.name + '.jpg'
        print(imgdir)
        imgkit.from_string(html, imgdir, options=OPTIONS)

# TODO
#  1) очистка дериктории с изображениями перед генерацией
#  2) генерация на А4 через imgkit
#  3) открыть директорию с изображениями после генерации


if __name__ == '__main__':
    transform_zettel_to_image()
