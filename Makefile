.PHONY: po mo

LANG_DIR = assets/language

po:
	xgettext -Lpython --output=$(LANG_DIR)/messages.pot main.py View/MainScreen/main_screen.kv
	msgmerge --update --no-fuzzy-matching --backup=off $(LANG_DIR)/po/en.po $(LANG_DIR)/messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off $(LANG_DIR)/po/fr.po $(LANG_DIR)/messages.pot

mo:
	mkdir -p $(LANG_DIR)/locales/en/LC_MESSAGES
	mkdir -p $(LANG_DIR)/locales/fr/LC_MESSAGES
	msgfmt -c -o $(LANG_DIR)/locales/en/LC_MESSAGES/langapp.mo $(LANG_DIR)/po/en.po
	msgfmt -c -o $(LANG_DIR)/locales/fr/LC_MESSAGES/langapp.mo $(LANG_DIR)/po/fr.po
