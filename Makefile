VERSION = 0.4.11

FILES = COPYING ChangeLog FAQ INSTALL Makefile README VERSION nomail \
	nomail.8 nomail.conf nomail.txt nosend nosend.8 nosend.txt \
	nomail.spec daemontools/ debian/

%.txt: %.8
	@nroff -man -Tnippon $< | w3m -dump > $@

txt: nomail.txt nosend.txt

TAGS: nomail nosend
	@etags -l perl nomail nosend

dist: nomail-$(VERSION).tar.gz

clean:
	@rm -f TAGS *.txt *~ *.tar.gz

nomail-$(VERSION).tar.gz: $(FILES)
	mkdir nomail-$(VERSION)
	cp -r $(FILES) nomail-$(VERSION)
	tar zcf $@ nomail-$(VERSION)
	rm -rf nomail-$(VERSION)

install:
	install -m 755 -d $(DESTDIR)/etc/nomail
	install -m 644 nomail.conf $(DESTDIR)/etc/nomail/nomail.conf
	install -m 700 -o nomail -d $(DESTDIR)/var/spool/nomail
	install -m 4711 -o nomail nomail $(DESTDIR)/usr/sbin
	install -m 4711 -o nomail nosend $(DESTDIR)/usr/bin
	(cd $(DESTDIR)/usr/sbin ; ln -s nomail sendmail)
