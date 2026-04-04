FILE =../flag
FLAG = $(shell cat $(FILE))
CC = gcc
ENC_FILE = flag.enc

all: main.c
	$(CC) -o ../public/crypto $^

main.c: obfuscate.c main.template.c
	gcc obfuscate.c -o obfuscate
	chmod +x obfuscate
	./obfuscate $(FLAG) > $(ENC_FILE)	
	$(eval ENC_FLAG := $(shell cat $(ENC_FILE)))
	sed 's/__TEMPLATE__/$(ENC_FLAG)/g' main.template.c > main.c

clean:
	rm -f ../public/main obfuscate $(ENC_FILE) main.c

