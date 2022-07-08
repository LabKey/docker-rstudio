build: labkey.ipynb labkey.echo

labkey.ipynb:
	docker build . -f Dockerfile -t labkey/nbconvert

labkey.echo: labkey.ipynb
	docker build . -f Dockerfile.echo -t labkey/echo
