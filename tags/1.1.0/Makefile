prefix=/usr/local
INSTALL=install -o root -g wheel -m 644
INSTALLX=install -o root -g wheel -m 755
botuser=freq
botgroup=freq
vardir=/var/freq
logdir=/var/log/freq
distname=freqbot
distver=1.1.0
rev=''
dist=$(distname)-$(distver)
tarballdir=..

build: doc lang templates tools
	@echo Building $(dist)...
	@$(MAKE) depends
	@$(MAKE) -C doc build version=$(distver).$(rev)
	@chmod -R u+w,u+r,o-w,o+r .

clean:
	@ echo Cleaning.
	@$(MAKE) -C doc clean
	@find . -name "*~" -delete
	@find . -name "*.pyc" -delete

depends: tools/depends.py
	@echo Checking if all dependencies installed
	@python tools/depends.py

install:
	@$(MAKE) build
	@echo -n "Copying files to $(prefix)/share/freq/: "
	@rm -rf $(prefix)/share/freq/src/
	@mkdir -p $(prefix)/share/freq
	@mkdir -p $(prefix)/etc/rc.d
	@$(INSTALL) README $(prefix)/share/freq
	@$(INSTALL) CHANGES $(prefix)/share/freq
	@$(INSTALL) COPYING $(prefix)/share/freq
	@$(INSTALLX) start.py $(prefix)/share/freq
	@$(INSTALL) config.defaults $(prefix)/share/freq
	@mkdir -p $(prefix)/share/freq/doc
	@cp -r doc/html $(prefix)/share/freq/doc/
	@cp -r doc/help $(prefix)/share/freq/doc/
	@cp -r doc/syntax $(prefix)/share/freq/doc/
	@cp -r lang $(prefix)/share/freq/
	@mkdir -p $(prefix)/share/freq/modules
	@$(INSTALL) modules/*.py $(prefix)/share/freq/modules
	@cp -r src $(prefix)/share/freq/
	@cp -r static $(prefix)/share/freq/
	@mkdir -p $(prefix)/share/freq/templates
	@$(INSTALL) templates/*.html $(prefix)/share/freq/templates/
	@cat src/kernel/freq.py | sed s/self.getRev\(\)/\'$(rev)\'/ >$(prefix)/share/freq/src/kernel/freq.py
	@rm -rf `find $(prefix)/share/freq -name ".svn"`
	@chown -R root:wheel $(prefix)/share/freq
	@find $(prefix)/share/freq -name "*.pyc" -delete
	@find $(prefix)/share/freq -name "*~" -delete
	@echo done.
	$(INSTALL) freq.conf.example $(prefix)/etc
	$(INSTALLX) tools/freqbot $(prefix)/etc/rc.d/freq
	@echo "Creating user && group:"
	@if pw groupshow -n $(botgroup) >/dev/null 2>&1; then echo " group $(botgroup) already exists: do nothing"; else pw groupadd -n $(botgroup); fi
	@if pw usershow -n $(botuser) >/dev/null 2>&1; then echo " user $(botuser) already exists: do nothing"; else pw useradd -n $(botuser) -g $(botgroup) -d /var/freq; fi
	@mkdir -p $(logdir)
	@chown -R $(botuser):$(botgroup) $(logdir)
	@mkdir -p $(vardir)
	@chown -R $(botuser):$(botgroup) $(vardir)
	@su freq -c "./tools/mkdata $(vardir)"
	@echo
	@echo "  $(dist) installed into $(prefix)"
	@echo
	@echo "  To start freQ-bot You need to:"
	@echo "    1) add freq_enable=\"YES\" to /etc/rc.conf"
	@echo "    2) copy $(prefix)/etc/freq.conf.example to $(prefix)/etc/freq.conf and EDIT IT"
	@echo "    3) start bot: $(prefix)/etc/rc.d/freq start"
	@echo "    4) if you want use .google, you need to create $(prefix)/share/freq/.googlekey and put your googlekey there"
	@echo

deinstall:
	rm -rf $(prefix)/share/freq
	rm -f $(prefix)/etc/rc.d/freq
	rm -f $(prefix)/etc/freq.conf.example
	@echo you can also remove "$(logdir) && $(vardir)"

userdel:
	pw userdel -n $(botuser)

tarball:
	@echo Cleaning
	@rm -rf $(tarballdir)/$(dist)
	@rm -f $(tarballdir)/$(dist).tar.bz2
	@cp -r . $(tarballdir)/$(dist)
	@find $(tarballdir)/$(dist) -name "*~" -delete
	@find $(tarballdir)/$(dist) -name "freq.conf" -delete
	@find $(tarballdir)/$(dist) -name "config.py" -delete
	@find $(tarballdir)/$(dist) -name "*.pyc" -delete
	@find $(tarballdir)/$(dist) -name ".svn" | xargs rm -rf
	@echo -n "Creating tarball: "
	@tar -C $(tarballdir) -cjf $(tarballdir)/$(dist).tbz $(dist)
	@echo $(tarballdir)/$(dist).tbz
	@rm -rf $(tarballdir)/$(dist)
	@echo done.
version:
	@echo $(dist)

sort:
	@tools/sort