#!/bin/bash -ex
TAG=$(date +%Y%m%d.%H%M)
docker build -f Dockerfile -t mair-ubuntu:"$TAG" .
