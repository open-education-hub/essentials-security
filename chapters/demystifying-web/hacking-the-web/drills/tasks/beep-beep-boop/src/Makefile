FILE	:=../flag
FLAG	:=$(shell cat $(FILE))

generate:
	rm -rf ../public
	mkdir -p ../public
	cp -r assets/ ../public
	cp index.html ../public
	cp robots.txt ../public
	sed 's/__TEMPLATE__/$(FLAG)/g' ./human-asimov.template.php > ../public/human-asimov.php

.PHONY: generate
