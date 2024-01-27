import gettext
from kivy.lang import Observable


class Language(Observable):
    observers = []
    lang = None

    def __init__(self, defaultlang):
        super(Language, self).__init__()
        self.ugettext = None
        self.lang = defaultlang
        self.switch_lang(self.lang)

    def _(self, text):
        return self.ugettext(text)

    def fbind(self, name, func, args, **kwargs):
        if name == "_":
            self.observers.append((func, args, kwargs))
        else:
            return super(Language, self).fbind(name, func, *args, **kwargs)

    def funbind(self, name, func, args, **kwargs):
        if name == "_":
            key = (func, args, kwargs)
            if key in self.observers:
                self.observers.remove(key)
        else:
            return super(Language, self).funbind(name, func, *args, **kwargs)

    def switch_lang(self, lang):
        locale_dir = "assets/languages_data/locales/"
        locales = gettext.translation('langapp', locale_dir, languages=[lang])

        self.ugettext = locales.gettext
        self.lang = lang

        # update all the kv rules attached to this text
        for func, largs, kwargs in self.observers:
            func(largs, None, None)


tr = Language("fr")
