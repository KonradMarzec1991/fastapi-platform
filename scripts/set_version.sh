#!/bin/bash

VERSION=$(cut -c1-7 /home/ec2-user/app/version.txt)
echo "APP_VERSION=$VERSION" > /home/ec2-user/app/.env