import os
import re


# filter to exclude notes from bibliographic list
ZETTELS_EXCLUDE = [
                  # '@51_18',
                 ]

ZETTELS_LIST = [
                # '@57',
                ]

# directory
ZETTELKASTENDIR = '/Users/dnv/Documents/Exocortex/Zettelkasten/'
IMGDIR = '/Users/dnv/Downloads/img_from_html/'

# subdirectory
SUBDIR = 'bibliographic_box/'
# SUBDIR = '_inbox/'

# options for imgkit generator
OPTIONS = {
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


def get_bibliographic_notes(path: str, exclude: list, all_notes=False):
    if all_notes:
        # get all files from  @bibliographic_box
        notes = sorted(os.listdir(path))
        if '@bibliographic_list.md' in notes:
            notes.remove('@bibliographic_list.md')
        return notes
    else:
        # get only files with format @31 and same, ignore @31_1
        notes = [f for f in os.listdir(path) if re.search(r'@\d+[a-zA-Z]*[.]', f)]
        # exclude files from notes
        return sorted(list((set(notes) - set(exclude))))


def get_notes(path: str, suffix: str):
    notes = []
    files = sorted(os.listdir(path))
    for file in files:
        if file.endswith(suffix):
            notes.append(file)
    return notes


def gen_html_view(name: str, content: str):
    style = """
            .zettel-borders {
               position: absolute;
               width: 421px;
               height: 298px;
               background: #FFFFFF;
               border: 1px dashed #D8D8D8;
               margin: 0;
               box-sizing: border-box;
            }
            .name {
               position: absolute;
               top: 12px;
               left: 14px;
               font-family: 'Inter';
               font-style: normal;
               font-weight: 400;
               font-size: 12px;
               line-height: 15px;
               color: #000000;
            }
            .content {
               position: absolute;
               width: 391px;
               top: 38px;
               left: 14px;
               font-family: 'Inter';
               font-style: normal;
               font-weight: 400;
               font-size: 12px;
               line-height: 15px;
               color: #000000;
            }
            .backlink {
               position: absolute;
               bottom: 11px;
               right: 14px;
               font-family: 'Inter';
               font-style: normal;
               font-weight: 400;
               font-size: 12px;
               line-height: 15px;
               color: #000000;
            }
    """

    html = f"""
    <!DOCTYPE HTML>
    <html lang="ru">
     <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <title>zettelkasten</title>
         <style>
            {style}
        </style>
     </head>
     <body class="zettel-borders">
    
      <div class="name">{name}</div>
      <div class="content">{content}</div>
      <div class="backlink"></div>
    
     </body>
    </html>"""
    return html
