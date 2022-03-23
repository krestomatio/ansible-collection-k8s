REPO_NAME ?= ansible-collection-k8s
VERSION ?= 0.0.85
PROJECT_SHORTNAME ?= k8s
PROJECT_TYPE ?= collection

CHANGELOG_LAST_TAG=v0.0.1

include hack/mk/main.mk
