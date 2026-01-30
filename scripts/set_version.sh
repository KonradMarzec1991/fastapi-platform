VERSION=$(cut -c1-7 version.txt)
echo "APP_VERSION=$VERSION" > /home/ec2-user/app/.env