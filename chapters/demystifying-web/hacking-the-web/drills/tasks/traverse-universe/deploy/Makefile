NAME := sss-essentials_05_traverse-the-universe
IMG_NAME := $(NAME)

EXTERNAL_PORT := 8015
INTERNAL_PORT := 80

build:
	docker build -t $(IMG_NAME) -f Dockerfile ..

run: build
	docker run -d \
		-p $(EXTERNAL_PORT):$(INTERNAL_PORT) \
		--name $(NAME) \
		$(IMG_NAME)

stop:
	docker stop $(NAME)

rm: stop
	docker rm $(NAME)

clean: rm
	docker image rm $(IMG_NAME):latest

.PHONY: build run stop rm clean
