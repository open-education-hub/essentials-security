NAME = unaccessible
INTERNAL_PORT = 80
EXTERNAL_PORT = 8001

.PHONY: build run stop clean

build:
docker build -t $(NAME) -f Dockerfile ..

run:
docker run -d -p $(EXTERNAL_PORT):$(INTERNAL_PORT) --name $(NAME) $(NAME)

stop:
docker stop $(NAME) || true
docker rm $(NAME) || true

clean: stop
docker rmi $(NAME) || true
