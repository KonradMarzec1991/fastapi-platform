VERSION=$(echo $DEPLOYMENT_ID | cut -c1-7)
echo "APP_VERSION=$VERSION" > /home/ec2-user/app/.env