import languages
from libs.moderat.Settings import Config


class Translate:

    def __init__(self):
        self.config = Config()
        if self.config.language in languages.__all__:
            lang = __import__('libs.languages.%s' % self.config.language, globals(), locals(), ['tr'], -1)
            self.tr = lang.tr
        else:
            self.tr = {}

    def word(self, _word):
        if self.tr.has_key(_word):
            return self.tr[_word]
        else:
            return _word