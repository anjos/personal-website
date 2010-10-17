# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
RSYNC_MASTER='andreps@andreanjos.org:my.andreanjos.org'
RSYNC=rsync --rsh=ssh --recursive --times --perms --owner --group --verbose --compress
PYTHON=python2.6

# A few helpers -- don't modify!
admin=sw/bin/djm $(1)

all: bootstrap 

.PHONY: clean restart mrproper generate_bootstrap bootstrap upgrade strings compile shell dbshell syncdb 

generate_bootstrap:
	$(MAKE) --directory=installer generate

bootstrap: generate_bootstrap
	@./installer/bootstrap.py --quiet --python=$(PYTHON) sw
	@cd sw/lib && if [ ! -L current ]; then ln -s $(PYTHON) current; fi && cd -

upgrade:
	@./installer/bootstrap.py --quiet --python=$(PYTHON) --upgrade sw
	@cd sw/lib && if [ ! -L current ]; then ln -s $(PYTHON) current; fi && cd -

restart:
	@skill -15 python

clean: 	
	@find . -name '*~' -print0 | xargs -0 rm -vf 

mrproper: clean
	@rm -rf sw pip-log.txt
	$(MAKE) --directory=installer mrproper 
	@find . -name '*.py?' -print0 | xargs -0 rm -vf

pull:
	@echo 'Pulling Git sources'
	git pull
	@echo 'Synchronize media directory'
	$(RSYNC) $(RSYNC_MASTER)/media ./
	@echo 'Re-compiling language files'
	$(MAKE) --directory=. compile
	@echo 'Synchronization is done'

push:
	@echo 'Pushing Git sources into master repository'
	git push
	@echo 'Synchronizing local media with that of master server'
	$(RSYNC) ./media/ $(RSYNC_MASTER)/media/

strings:
	@cd portal/portal; ../../$(call admin,makemessages --all --extension=html,py,txt);

compile: strings
	@cd portal/portal; ../../$(call admin,compilemessages);

validate:
	$(call admin,validate)

syncdb: validate
	$(call admin,syncdb)

shell:
	$(call admin,shell)

dbshell:
	$(call admin,dbshell)

test: compile validate syncdb
	$(call admin,runserver 8080)

smtp:
	$(python) -m smtpd -n -c DebuggingServer localhost:1025

