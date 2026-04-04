FILE	:=../flag
FLAG	:=$(shell cat $(FILE))

generate:
	rm -rf ../public
	mkdir -p ../public/colours
	sed 's/__TEMPLATE__/$(FLAG)/g' index.template.php > ../public/colours/index.php

.PHONY: generate
