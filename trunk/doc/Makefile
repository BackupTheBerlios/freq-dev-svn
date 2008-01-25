version="unknown version"

clean:
	@rm -rf html

html: help/* ../tools/builddoc.py ../templates/*
	@echo Building HTML docs
	@$(MAKE) clean
	@mkdir html
	@python ../tools/builddoc.py help html ../templates $(version) || rm -rf html

build: html

