IMAGE_TAG = "fullcycle-hello-go"

build_app:
	rm -f build/hello
	go build -o build/hello hello.go

build_docker_image: build
	docker build . -t $(IMAGE_TAG)

upload_docker_image: build_docker_image
	docker tag $(IMAGE_TAG) elyssonmr/$(IMAGE_TAG):latest
	docker push elyssonmr/$(IMAGE_TAG)
