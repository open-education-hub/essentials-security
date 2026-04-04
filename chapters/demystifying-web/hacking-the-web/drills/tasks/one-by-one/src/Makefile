FILE :=../flag
FLAG :=$(shell cat $(FILE))

generate:
	rm -rf ../public
	mkdir -p ../public/one-by-one
	sed 's/__TEMPLATE__/$(FLAG)/g' index.template.php > ../public/one-by-one/index.php

.PHONY: generate
