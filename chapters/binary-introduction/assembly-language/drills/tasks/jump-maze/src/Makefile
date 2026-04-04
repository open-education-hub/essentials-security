OBJ_FILE = ../public/jump_maze.o

all:
	rm -rf ../public
	python3 generate_asm_file.py
	nasm -f elf64 -o $(OBJ_FILE) jump_maze.asm
	strip $(OBJ_FILE)

.PHONY: all
