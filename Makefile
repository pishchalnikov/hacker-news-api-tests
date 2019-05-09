PYTEST_CACHE_DIR=/tmp/

STAGING_HOST ?= hacker-news.firebaseio.com
STAGING_PORT ?= 443

DOCKER_IMAGE := hacker-news-api-tests
DOCKER_TAG ?= latest
DOCKER_NOROOT := -u $$(id -u):$$(id -g)
DOCKER_FLAGS := --rm=true $(DOCKER_NOROOT) \
				-v $(PWD):/tests \
				-w /tests \
				--network=host
DOCKER_ENV := --env STAGING_HOST=${STAGING_HOST} \
			  --env STAGING_PORT=${STAGING_PORT} \


.PHONY: all

all:
	$(MAKE) docker-build
	$(MAKE) docker-lint
	$(MAKE) docker-test

test:
	python3 -m pytest -o cache_dir=${PYTEST_CACHE_DIR}

lint:
	flake8 --exclude=.venv

docker-build:
	docker build --pull --rm --tag "$(DOCKER_IMAGE):$(DOCKER_TAG)" .

docker-test:
	docker run $(DOCKER_FLAGS) $(DOCKER_ENV) "$(DOCKER_IMAGE):$(DOCKER_TAG)" \
	make test

docker-lint:
	docker run $(DOCKER_FLAGS) $(DOCKER_ENV) "$(DOCKER_IMAGE):$(DOCKER_TAG)" \
	make lint

docker-clean:
	docker rmi -f "$$(docker images -q $(DOCKER_IMAGE):$(DOCKER_TAG))"
