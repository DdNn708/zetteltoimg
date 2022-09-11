import imgkit

from config import ZETTELS_LIST, ZETTELKASTENDIR, SUBDIR, IMGDIR, gen_html_view
from utils.zettel import Zettel

# options for imgkit generator
options = {
    # on default dpi=96. I need 300 dpi, that's why I set zoom = 3 and multiplied width and height to 3
    'zoom': 3,
    'height': 298 * 3,
    'width': 421 * 3,
    'quality': 100,
    'disable-smart-width': None,
    'encoding': "UTF-8",
    # 'enable-local-file-access': None,
    # 'crop-h': '3',
    # 'crop-w': '3',
    # 'crop-x': '3',
    # 'crop-y': '3',
}

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
    imgkit.from_string(html, imgdir, options=options)

# TODO
#  1) очистка дериктории с изображениями перед генерацией
#  2) генерация на А4 через imgkit
#  3) открыть директорию с изображениями после генерации
