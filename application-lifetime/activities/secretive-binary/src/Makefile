LIB = hide_flag
PATCH = patch
BIN = secretive

all: lib$(LIB).so $(BIN)

$(BIN): $(BIN).c
	$(CC) $^ -L. -l$(LIB) -o $@

lib$(LIB).so: $(LIB).c
	$(CC) -shared -fPIC $^ -o $@

clean:
	rm $(BIN) *.o *.so

.PHONY: all clean
