REPO_NAME ?= ansible-collection-k8s
REPO_OWNER ?= krestomatio
VERSION ?= 0.0.15

# JX
JOB_NAME ?= sanity
PULL_NUMBER ?= 0
BUILD_ID ?= 0

# Build
ifeq ($(JOB_NAME),release)
BUILD_VERSION ?= $(shell git rev-parse HEAD^2 &>/dev/null && git rev-parse HEAD^2 || echo)
else
BUILD_VERSION ?= $(shell git rev-parse HEAD 2> /dev/null  || echo)
endif

# CI
SKIP_MSG := skip.ci
RUN_PIPELINE ?= $(shell git log -1 --pretty=%B | cat | grep -q "\[$(SKIP_MSG)\]" && echo || echo 1)
ifeq ($(RUN_PIPELINE),)
SKIP_PIPELINE = true
$(info RUN_PIPELINE not set, skipping...)
endif
ifeq ($(BUILD_VERSION),)
SKIP_PIPELINE = true
$(info BUILD_VERSION not set, skipping...)
endif
ifeq ($(origin PULL_BASE_SHA),undefined)
CHANGELOG_FROM ?= HEAD~1
else
CHANGELOG_FROM ?= $(PULL_BASE_SHA)
endif

# Release
GIT_REMOTE ?= origin
GIT_BRANCH ?= master
GIT_ADD_FILES ?= Makefile
CHANGELOG_FILE ?= CHANGELOG.md

# Promote
UPDATEBOT_M4E_ONLY_MSG := chore(m4e): bump image versions with updatebot
ifeq (,$(shell git log -1 --pretty=%B | cat | grep -q "$(UPDATEBOT_M4E_ONLY_MSG)" && echo || echo 1))
UPDATEBOT_CONFIG_FILE ?= .lighthouse/updatebot-m4e-only.yaml
else
UPDATEBOT_CONFIG_FILE ?= .lighthouse/updatebot.yaml
endif

all: sanity

##@ General

# The help target prints out all targets with their descriptions organized
# beneath their categories. The categories are represented by '##@' and the
# target descriptions by '##'. The awk commands is responsible for reading the
# entire set of makefiles included in this invocation, looking for lines of the
# file as xyz: ## something, and then pretty-format the target and help. Then,
# if there's a line with ##@ something, that gets pretty-printed as a category.
# More info on the usage of ANSI control characters for terminal formatting:
# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
# More info on the awk command:
# http://linuxcommand.org/lc3_adv_awk.php

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: git
git: ## Git add, commit, tag and push
	git add $(GIT_ADD_FILES)
	git commit -m "chore(release): $(VERSION)" -m "[$(SKIP_MSG)]"
	git tag v$(VERSION)
	git push $(GIT_REMOTE) $(GIT_BRANCH) --tags

.PHONY: galaxy-version
galaxy-version: ## Bump galaxy version
	sed -i "s/^version:.*/version: $(VERSION)/" galaxy.yml
	git add galaxy.yml

.PHONY: galaxy-publish
galaxy-publish: ## Publish galaxy collection
	ansible-galaxy collection build --force
	$(info ansible-galaxy collection publish krestomatio-k8s-$(VERSION).tar.gz)
	@ansible-galaxy collection publish krestomatio-k8s-$(VERSION).tar.gz --api-key $(ANSIBLE_GALAXY_TOKEN)

.PHONY: start-dockerd
start-dockerd: ## Start docker daemon in background (if not running) (meant to be run in container)
ifeq (,$(shell pidof dockerd))
	$(info starting dockerd in the backgroud...)
	dockerd-entrypoint.sh &> /tmp/dockerd.log &
	@sleep 4
else
	$(info dockerd already running...)
endif

.PHONY: ansible-lint
ansible-lint: ## Ansible linting
	ansible-lint roles/

##@ JX

.PHONY: jx-changelog
jx-changelog: ## Generate changelog file using jx
ifeq (0, $(shell test -d  "charts/$(REPO_NAME)"; echo $$?))
	sed -i "s/^version:.*/version: $(VERSION)/" charts/$(REPO_NAME)/Chart.yaml
	sed -i "s/tag:.*/tag: $(VERSION)/" charts/$(REPO_NAME)/values.yaml
	sed -i "s@repository:.*@repository: $(IMG_NAME)@" charts/$(REPO_NAME)/values.yaml
	git add charts/
else
	echo no charts
endif
	jx changelog create --verbose --version=$(VERSION) --rev=$(CHANGELOG_FROM) --output-markdown=$(CHANGELOG_FILE) --update-release=false
	git add $(CHANGELOG_FILE)

.PHONY: jx-updatebot
jx-updatebot: ## Create PRs in downstream repos with new version using jx
	jx-updatebot pr -c $(UPDATEBOT_CONFIG_FILE) \
		--commit-title "chore(update): bump collection krestomatio.k8s $(VERSION)" \
		--labels test_group \
		--version $(VERSION)

##@ Tests

.PHONY: test-sanity
test-sanity: ## Run sanity test with ansible-test
	ansible-test sanity --docker default

# CI tasks
## start if not SKIP_PIPELINE
ifeq ($(origin SKIP_PIPELINE),undefined)

##@ Pullrequest

.PHONY: sanity
sanity: ansible-lint start-dockerd test-sanity ## Run sanity tests

##@ Release

.PHONY: changelog
changelog: jx-changelog ## Generate changelog

.PHONY: release
release: galaxy-version galaxy-publish ## Run release tasks

.PHONY: promote
promote: jx-updatebot git ## Promote release

## else if not SKIP_PIPELINE
else
$(info SKIP_PIPELINE set:)
## Pull request
sanity:
	$(info skipping sanity...)

## Release
changelog:
	$(info skipping changelog...)

release:
	$(info skipping release...)

promote:
	$(info skipping promote...)

## end if not SKIP_PIPELINE
endif
