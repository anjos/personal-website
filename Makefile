# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
RSYNC_MASTER='andreps@andreanjos.org:my.andreanjos.org'
RSYNC=rsync --rsh=ssh --recursive --times --perms --owner --group --verbose --compress
PYTHON=python2.6

# A few helpers -- don't modify!
admin=bin/django $(1)

all: bootstrap

.PHONY: clean restart mrproper generate_bootstrap bootstrap upgrade strings compile shell dbshell syncdb run

bootstrap: generate_bootstrap
	@python bootstrap.py
	@bin/buildout

restart:
	@skill -15 python

clean:
	@find -L . -name '*~' -print0 | xargs -0 rm -vf 

mrproper: clean
	@rm -rf sw pip-log.txt
	$(MAKE) --directory=installer mrproper 
	@find -L . -name '*.py?' -print0 | xargs -0 rm -vf
	@find -L . -name '*.egg-info' -print0 | xargs -0 rm -rvf

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
	@cd portal; ../$(call admin,makemessages --all --extension=html,py,txt);

compile: strings
	@cd portal; ../$(call admin,compilemessages);

validate:
	$(call admin,validate)

syncdb: validate
	$(call admin,syncdb)

shell:
	$(call admin,shell)

dbshell:
	$(call admin,dbshell)

run:
	$(call admin,runserver 8080)

test: compile syncdb run

smtp:
	$(python) -m smtpd -n -c DebuggingServer localhost:1025
