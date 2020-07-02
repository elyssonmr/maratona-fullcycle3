IMAGE_TAG = "fullcycle-hello-buffalo"
EXE_NAME = "desafio02"

build_app:
	buffalo build -o build/

build_docker_image:
	docker build . -t $(IMAGE_TAG)

upload_docker_image: build_docker_image
	docker tag $(IMAGE_TAG) elyssonmr/$(IMAGE_TAG):latest
	docker push elyssonmr/$(IMAGE_TAG)
