FILE	:=../flag
FLAG	:=$(shell cat $(FILE))

generate:
	rm -rf ../public
	mkdir -p ../public/produce-consume
	cp -r ./* ../public/produce-consume
	sed 's/__TEMPLATE__/$(FLAG)/g' consume.template.php > ../public/produce-consume/consume.php
	rm ../public/produce-consume/*template*

.PHONY: generate
