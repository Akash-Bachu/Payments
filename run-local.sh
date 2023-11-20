#!/bin/bash

docker build -t bramble-EasyPay .
docker run -p 8501:8501 bramble-EasyPay
