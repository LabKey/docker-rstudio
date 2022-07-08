
The original idea was to run reports using the equivalent of "docker run --rm -i labkey/ipynb".  I haven't quite figured that out yet on the docker-java side because of stdin/stdout handling.  What I am doing is more like

docker run --rm -d labkey/ipynb
docker exec -i {imagename} /execute
docker stop {imagename} 

That is why the ENTRYPOINT command is a dummy wait loop.  This may change.
