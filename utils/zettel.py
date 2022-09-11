import markdown


class Zettel:
    def __init__(self):
        self.name: str = None  # zettel-file name can be with extension
        self.path = None  # path to zettelfile
        self.content = None  # in html or text format
        self.backlinks = None
        self.extension = None

    def set_name(self, name: str):
        # if filename with extension, will take only filename
        if '.' in name:
            splited = name.split(sep='.')
            self.name = splited[0]
            self.extension = '.' + splited[1].lower()
        else:
            self.name = name

    def set_path(self, path: str):
            self.path = path + self.name + self.extension

    def set_path_v2(self, path: str):
            self.path = path + self.name + '.md'

    def set_html_content(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            md_text = f.read()

            # convert md to html format
            self.content = markdown.markdown(md_text)

    def set_text_content(self):
        if self.extension == '.md' and '_' not in self.name:
            with open(self.path, 'r', encoding='utf-8') as f:
                text = f.read()
                self.content = text.strip('\n')
        else:
            self.content = ''

    def __repr__(self):
        return f'{self.name}'


