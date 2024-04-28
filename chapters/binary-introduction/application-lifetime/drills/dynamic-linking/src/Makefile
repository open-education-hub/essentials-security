CFLAGS = -fPIC
BIN = dynamic-linked
LIB = hello

all: $(BIN)

$(BIN): lib$(LIB).so main.o
	$(CC) main.o -L. -l$(LIB) -o $@

lib$(LIB).so: $(LIB).o
	$(CC) -shared $^ -o $@

$(LIB).o: $(LIB).c

main.o: main.c

clean:
	rm $(BIN) *.o *.so

.PHONY: all clean
