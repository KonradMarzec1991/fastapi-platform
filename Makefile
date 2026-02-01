# ===== CONFIG =====
APP_NAME := fastapi-demo
AWS_REGION := us-east-1
AWS_ACCOUNT_ID := 622711946516

ECR_REPO := $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(APP_NAME)
GIT_BRANCH := master

# commit hash (krótki)
GIT_SHA := $(shell git rev-parse --short HEAD)

# ===== PHONY =====
.PHONY: help docker-build docker-push docker run push-all

# ===== HELP =====
help:
	@echo "Available targets:"
	@echo "  docker        Build & push Docker image to ECR"
	@echo "  run           Run FastAPI locally"
	@echo "  push-all      Push code to GitHub and CodeCommit"

# ===== DOCKER =====
docker-build:
	docker build -t $(APP_NAME):$(GIT_SHA) .

docker-push: docker-build
	aws ecr get-login-password --region $(AWS_REGION) | \
	docker login --username AWS --password-stdin $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com
	docker tag $(APP_NAME):$(GIT_SHA) $(ECR_REPO):$(GIT_SHA)
	docker push $(ECR_REPO):$(GIT_SHA)

docker: docker-push

# ===== LOCAL RUN =====
run:
	fastapi run app.py

# ===== GIT =====
push-all:
	git push origin $(GIT_BRANCH)
	git push aws $(GIT_BRANCH)