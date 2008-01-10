prefix=/usr/local
INSTALL=install -o root -g wheel -m 644
INSTALLX=install -o root -g wheel -m 755
botuser=freq
botgroup=freq

clean:
	#Cleaning
	$(MAKE) -C doc clean
	find . -name "*~" -delete

depends: tools/depends.py
	python tools/depends.py

build: doc lang templates tools
	$(MAKE) depends
	$(MAKE) -C doc build
	chmod -R u+w,u+r,o-w,o+r .

install:
	$(MAKE) build
	#copying files..
	mkdir -p $(prefix)/share/freq
	mkdir -p $(prefix)/etc/rc.d
	$(INSTALL) README $(prefix)/share/freq
	$(INSTALL) CHANGES $(prefix)/share/freq
	$(INSTALLX) start.py $(prefix)/share/freq
	$(INSTALL) config.defaults $(prefix)/share/freq
	$(INSTALL) freq.conf.example $(prefix)/etc
	mkdir -p $(prefix)/share/freq/doc
	cp -r doc/html $(prefix)/share/freq/doc/
	cp -r doc/help $(prefix)/share/freq/doc/
	cp -r doc/syntax $(prefix)/share/freq/doc/
	cp -r lang $(prefix)/share/freq/
	mkdir -p $(prefix)/share/freq/modules
	$(INSTALL) modules/*.py $(prefix)/share/freq/modules
	cp -r src $(prefix)/share/freq/
	mkdir -p $(prefix)/share/freq/templates
	$(INSTALL) templates/*.html $(prefix)/share/freq/templates/
	cp -r src $(prefix)/share/freq/
	rm -rf `find $(prefix)/share/freq -name ".svn"`
	chown -R root:wheel $(prefix)/share/freq
	#rc script
	$(INSTALLX) tools/freqbot $(prefix)/etc/rc.d/freq
	#user, var..
	if pw groupshow -n $(botgroup) 2>/dev/null; then echo group $(botgroup) already exists..; else pw groupadd -n $(botgroup); fi
	if pw usershow -n $(botuser) 2>/dev/null; then echo user $(botuser) already exists..; else pw useradd -n $(botuser) -g $(botgroup) -d /var/freq; fi
	mkdir -p /var/log/freq
	chown -R $(botuser):$(botgroup) /var/log/freq
	mkdir -p /var/freq
	chown -R $(botuser):$(botgroup) /var/freq
	echo "freQ installed to $(prefix)"

deinstall:
	rm -rf $(prefix)/share/freq
	rm -f $(prefix)/etc/rc.d/freq
	rm -f $(prefix)/etc/freq.conf.example
	echo "you can also remove /var/log/freq && /var/freq"

userdel:
	pw userdel -n $(botuser)
