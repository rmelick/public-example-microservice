# this script just builds and tags the docker image
TAG=rmelickvida/public-example-microservice:$(git rev-parse --short HEAD)
docker build -t ${TAG} .
docker push ${TAG}
