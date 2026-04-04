PORT := 31222
IMG_NAME := sss-essentials-01_whats-running
CONT_NAME := ${IMG_NAME}

compile:
	make -C ../src

build:
	docker build -t $(IMG_NAME) -f Dockerfile ..

run: compile build
	docker run -d -p $(PORT):22 --name $(CONT_NAME) -t $(IMG_NAME)

stop:
	docker stop $(CONT_NAME)

clean: stop
	make -C ../src clean
	docker rm $(IMG_NAME)
	docker image rm $(IMG_NAME):latest

.PHONY: build run stop clean
