CFLAGS = -fPIC
BIN = main
LIB = puts

all: $(LIB).so $(BIN)

$(LIB).so: $(LIB).o
	$(CC) -shared -fPIC $^ -o $@

clean:
	rm $(BIN) *.o *.so

.PHONY: all clean
