CC = movcc
BIN = ghidra_killer
SHELL := /bin/bash
MOVCC_PATH = /tmp/movfuscator
PREPARE = /tmp/.prepare

all: $(PREPARE) $(BIN)

$(BIN): $(BIN).c

$(PREPARE):
	git clone https://github.com/xoreaxeaxeax/movfuscator $(MOVCC_PATH) 2> /dev/null && \
	pushd $(MOVCC_PATH) && \
	./build.sh && \
	sudo mv build/movcc /usr/local/bin/ && \
	popd && \
	touch $(PREPARE)

$(BIN): $(BIN).c

clean:
	rm -rf $(BIN)
