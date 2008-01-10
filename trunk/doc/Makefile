clean:
	rm -rf html

html: help/* ../tools/builddoc.py ../templates/*
	#Building HTML docs...
	$(MAKE) clean
	mkdir html
	python ../tools/builddoc.py help html ../templates || rm -rf html

build: html

