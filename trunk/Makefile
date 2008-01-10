clean:
	#Cleaning
	$(MAKE) -C doc clean

depends: tools/depends.py
	python tools/depends.py

build: doc lang templates tools
	$(MAKE) depends
	$(MAKE) -C doc build

install:
	$(MAKE) build
	#copying files..
	#...
	#rc script
	#...
	#user, var..
	#...
	echo "freQ installed to $(PREFIX)"
	echo $(python)