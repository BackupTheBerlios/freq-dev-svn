prefix=/usr/local
INSTALL=install -o root -g wheel -m 644
INSTALLX=install -o root -g wheel -m 755
botuser=freq
botgroup=freq
vardir=/var/freq
logdir=/var/log/freq
distname=freqbot
distver=1.0.99
rev=`tools/getrev 2>/dev/null`
dist=$(distname)-$(distver).$(rev)
tarballdir=..

build: doc lang templates tools
	echo Building $(dist)
	$(MAKE) depends
	$(MAKE) -C doc build version=$(distver).$(rev)
	chmod -R u+w,u+r,o-w,o+r .

clean:
	#Cleaning
	$(MAKE) -C doc clean
	find . -name "*~" -delete
	find . -name "*.pyc" -delete

depends: tools/depends.py
	python tools/depends.py

install:
	$(MAKE) build
	#copying files..
	rm -rf $(prefix)/share/freq/src/
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
	cp -r static $(prefix)/share/freq/
	mkdir -p $(prefix)/share/freq/templates
	$(INSTALL) templates/*.html $(prefix)/share/freq/templates/
	cp -r src $(prefix)/share/freq/
	cat src/kernel/freq.py | sed s/self.getRev\(\)/\'$(rev)\'/ >$(prefix)/share/freq/src/kernel/freq.py
	rm -rf `find $(prefix)/share/freq -name ".svn"`
	chown -R root:wheel $(prefix)/share/freq
	find $(prefix)/share/freq -name "*.pyc" -delete
	find $(prefix)/share/freq -name "*~" -delete
	
	#rc script
	$(INSTALLX) tools/freqbot $(prefix)/etc/rc.d/freq
	#user, var..
	if pw groupshow -n $(botgroup) 2>/dev/null; then echo group $(botgroup) already exists..; else pw groupadd -n $(botgroup); fi
	if pw usershow -n $(botuser) 2>/dev/null; then echo user $(botuser) already exists..; else pw useradd -n $(botuser) -g $(botgroup) -d /var/freq; fi
	mkdir -p $(logdir)
	chown -R $(botuser):$(botgroup) $(logdir)
	mkdir -p $(vardir)
	chown -R $(botuser):$(botgroup) $(vardir)
	su freq -c "./tools/mkdata $(vardir)"
	echo " === $(dist) installed into $(prefix) ==="

deinstall:
	rm -rf $(prefix)/share/freq
	rm -f $(prefix)/etc/rc.d/freq
	rm -f $(prefix)/etc/freq.conf.example
	echo you can also remove $(logdir) && $(vardir)

userdel:
	pw userdel -n $(botuser)

tarball:
	rm -rf $(tarballdir)/$(dist)
	rm -f $(tarballdir)/$(dist).tar.bz2
	cp -r . $(tarballdir)/$(dist)
	find $(tarballdir)/$(dist) -name "*~" -delete
	find $(tarballdir)/$(dist) -name "freq.conf" -delete
	find $(tarballdir)/$(dist) -name "config.py" -delete
	find $(tarballdir)/$(dist) -name "*.pyc" -delete
	find $(tarballdir)/$(dist) -name ".svn" | xargs rm -rf
	tar -C $(tarballdir) -cjf $(tarballdir)/$(dist).tar.bz2 $(dist)
	rm -rf $(tarballdir)/$(dist)

version:
	echo $(dist)