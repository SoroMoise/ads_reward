.PHONY: po mo

po:
	xgettext -Lpython --output=messages.pot main.py View/MainScreen/main_screen.kv
	msgmerge --update --no-fuzzy-matching --backup=off po/en.po messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off po/fr.po messages.pot

mo:
	mkdir -p assets/languages_data/locales/en/LC_MESSAGES
	mkdir -p assets/languages_data/locales/fr/LC_MESSAGES
	msgfmt -c -o assets/languages_data/locales/en/LC_MESSAGES/langapp.mo po/en.po
	msgfmt -c -o assets/languages_data/locales/fr/LC_MESSAGES/langapp.mo po/fr.po
