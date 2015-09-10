#!/usr/bin/make
PYTHON := /usr/bin/env python
EXTRA  := 


clean:
	rm -f .coverage
	find . -name '*.pyc' -delete
	rm -rf .venv
	(which dh_clean && dh_clean) || true

.venv:
	dpkg -s gcc python-dev python-virtualenv python-apt || \
	    sudo apt-get install -y gcc python-dev python-virtualenv python-apt
	virtualenv .venv --system-site-packages
	.venv/bin/pip install -I -r test-requirements.txt

lint:   .venv
	.venv/bin/flake8 --exclude hooks/charmhelpers hooks/* tests unit_tests
	@charm proof

test:  clean .venv
	@echo Starting unit tests...
	.venv/bin/nosetests -s --nologcapture --with-coverage $(EXTRA) unit_tests/

functional_test:
	@echo Starting amulet tests...
	@juju test -v -p AMULET_HTTP_PROXY --timeout 900
