PORT := 32122
IMG_NAME := sss-essentials-02_find-us-if-you-can
CONT_NAME := ${IMG_NAME}

build:
	docker build -t $(IMG_NAME) -f Dockerfile ..

run: build
	docker run -d -p $(PORT):22 --name $(CONT_NAME) -t $(IMG_NAME)

stop:
	docker stop $(CONT_NAME)

clean: stop
	docker rm $(IMG_NAME)
	docker image rm $(IMG_NAME):latest

.PHONY: build run stop clean
