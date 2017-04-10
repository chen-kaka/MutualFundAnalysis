cd /xy/src/MutualFundAnalysis/
ver=`date +%Y%m%d%H%M`
docker build -t MutualFundAnalysis:$ver .
containerId=`docker ps | grep MutualFundAnalysis: | awk '{print $1}'`
imageId=`docker ps | grep MutualFundAnalysis: | awk '{print $2}'`
if [ -n "$containerId" ]; then
  docker stop $containerId
  docker rm $containerId
fi
if [ -n "$imageId" ]; then
  docker rmi $imageId
fi

docker run  -d -p 8000:8000 \
    --name=MutualFundAnalysis-$ver MutualFundAnalysis:$ver
