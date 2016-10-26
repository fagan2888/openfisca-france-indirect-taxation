IGNORE_OPT=--ignore-files='(tests_aids_categ.py|test_carburants_builder.py|test_categorie_fiscale.py|test_depenses_caburants_ht.py|test_get_poste_categorie_fiscale.py|test_legislations.py|test_simulation.py|test_survey_scenario.py|test_aliss_survey_scenario.py)'
TESTS_DIR=openfisca_france_indirect_taxation/tests

all: flake8 test

check-syntax-errors:
	@# This is a hack around flake8 not displaying E910 errors with the select option.
	@# Do not analyse .gitignored files.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	test -z "`flake8 --first $(shell git ls-files | grep "\.py$$") | grep E901`"

clean-pyc:
	find -name '*.pyc' -exec rm \{\} \;

ctags:
	ctags --recurse=yes .

flake8: clean-pyc
	flake8

test: check-syntax-errors
	nosetests $(TESTS_DIR) --stop --with-doctest

test-ci: check-syntax-errors
	nosetests $(TESTS_DIR) $(IGNORE_OPT) --with-doctest

test-with-coverage:
	nosetests $(TESTS_DIR) $(IGNORE_OPT) --stop --with-coverage --cover-package=openfisca_france --cover-erase --cover-branches --cover-html
