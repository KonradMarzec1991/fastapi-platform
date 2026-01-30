#!/bin/bash

set -e
VERSION=$(head -c 7 /home/ec2-user/app/version.txt)
echo "APP_VERSION=$VERSION" > /home/ec2-user/app/.env