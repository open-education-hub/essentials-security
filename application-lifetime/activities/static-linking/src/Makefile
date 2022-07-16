BIN = main
LIB = hello

all: $(BIN)

$(BIN): lib$(LIB).a $(BIN).o
	$(CC) -static $(BIN).o -L. -l$(LIB) -o $@

lib$(LIB).a: $(LIB).o
	ar rcs $@ $^

$(LIB).o: $(LIB).c

$(BIN).o: $(BIN).c

clean:
	rm $(BIN) *.o *.a

.PHONY: all clean
