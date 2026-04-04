PORT := 8069
IMG_NAME := sss-essentials-03_pinger
CONT_NAME := ${IMG_NAME}

build:
	docker build -f Dockerfile -t $(IMG_NAME) ..

run: build
	docker run -d -p $(PORT):80 --name $(CONT_NAME) $(IMG_NAME)

stop:
	docker stop $(CONT_NAME)

clean: stop
	docker rm $(IMG_NAME)
	docker image rm $(IMG_NAME):latest

.PHONY: build run stop clean
