from utils.zettel import Zettel
from config import ZETTELKASTENDIR, SUBDIR, ZETTELS_EXCLUDE, get_bibliographic_notes
from datetime import datetime

path = f'{ZETTELKASTENDIR}{SUBDIR}'
notes = get_bibliographic_notes(path=path, exclude=ZETTELS_EXCLUDE, all_notes=True)

with open(f"{path}@bibliographic_list.md", "w") as f:
    f.write('')

name = ''
line = []
for z in notes:
    # create zettel and set parameters
    zettel = Zettel()
    zettel.set_name(z)
    zettel.set_path(f'{ZETTELKASTENDIR}{SUBDIR}')
    zettel.set_text_content()

    if name == '' and '_' not in zettel.name:
        name = zettel.name
        with open(f'{path}@bibliographic_list.md', 'a') as f:
            f.write(f'\n[[{zettel.name}]]    {zettel.content}\n')
        continue

    if '_' in zettel.name and name in zettel.name:
        line.append(f'[[{zettel.name}]]')
        # line.append(f'[[{zettel.name}]]{zettel.extension}')
        continue

    if '_' not in zettel.name and name != zettel.name:
        name = zettel.name
        with open(f'{path}@bibliographic_list.md', 'a') as f:
            f.write(', '.join(line) + '\n\n')
            line.clear()
            f.write(f'\n[[{zettel.name}]]    {zettel.content}\n')

# show exclude files in the end of the document
with open(f'{path}@bibliographic_list.md', 'a') as f:
    exclude = ', '.join(ZETTELS_EXCLUDE)

    f.write("\n---:datetime:---\n")
    f.write(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

    f.write("\n---:exclude:---\n")
    f.write(exclude)
