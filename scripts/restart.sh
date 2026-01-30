#!/bin/bash

export APP_VERSION=$(git rev-parse --short HEAD)
systemctl restart fastapi