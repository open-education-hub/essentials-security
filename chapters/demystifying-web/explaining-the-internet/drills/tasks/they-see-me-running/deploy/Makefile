PORT := 33180
IMG_NAME := sss-essentials-03_they-see-me-running
CONT_NAME := ${IMG_NAME}

build: server
	docker build -t $(IMG_NAME) -f Dockerfile ..

server:
	make -C ../src

run: build
	docker run -d -p $(PORT):80 --name $(CONT_NAME) -t $(IMG_NAME)

stop:
	docker stop $(CONT_NAME)

clean: stop
	make -C ../src clean
	docker rm $(IMG_NAME)
	docker image rm $(IMG_NAME):latest

.PHONY: build run stop clean
