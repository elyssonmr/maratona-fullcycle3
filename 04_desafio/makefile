IMAGE_TAG = "fullcycle-aulas-maratona"

build_docker_image:
	docker build . -t $(IMAGE_TAG)

upload_docker_image: build_docker_image
	docker tag $(IMAGE_TAG) elyssonmr/$(IMAGE_TAG):latest
	docker push elyssonmr/$(IMAGE_TAG)
