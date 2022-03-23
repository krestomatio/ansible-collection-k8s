REPO_NAME ?= ansible-collection-k8s
VERSION ?= 0.0.88
PROJECT_SHORTNAME ?= k8s
PROJECT_TYPE ?= collection

GIT_RELEASE_LAST_TAG=v0.0.1

include hack/mk/main.mk
