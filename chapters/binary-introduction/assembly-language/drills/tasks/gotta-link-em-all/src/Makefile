FILE =../flag
FLAG = $(shell cat $(FILE))
ENC_FILE = flag.enc
ASFLAGS = -f elf64

all: f1.asm f2.asm f3.asm get_flag_part.c
	nasm $(ASFLAGS) -o ../public/f1.o f1.asm
	nasm $(ASFLAGS) -o ../public/f2.o f2.asm
	nasm $(ASFLAGS) -o ../public/f3.o f3.asm
	gcc -c -o ../public/get_flag_part.o -O3 get_flag_part.c

get_flag_part.c: get_flag_part.template.c obfuscate.c
	gcc obfuscate.c -o obfuscate
	chmod +x obfuscate
	./obfuscate $(FLAG) > $(ENC_FILE)	
	$(eval ENC_FLAG := $(shell cat $(ENC_FILE)))
	sed 's/__TEMPLATE__/$(ENC_FLAG)/g' get_flag_part.template.c > get_flag_part.c

clean:
	rm -f ../public/*.o get_flag_part.c obfuscate $(ENC_FILE)

.PHONY: all clean
