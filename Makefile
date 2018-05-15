TRAVIS_REPO_SLUG ?= fernandoe/openedx-lms
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

shell:
	docker run -it \
			-v ${PWD}/edx-platform:/edx/app/edxapp/edx-platform \
			-v ${PWD}/lms:/lms \
			--rm '${TRAVIS_REPO_SLUG}:${TAG}' env TERM=$(TERM) bash

shell-baseimage:
	docker run -it --rm edxops/edxapp:latest env TERM=$(TERM) bash
