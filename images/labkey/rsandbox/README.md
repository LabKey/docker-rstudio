labkey/rsandbox:latest
======

Dockerfile for building Dockerized LabKey R image using with the latest R release version. 

Run `make rsandbox` from `images/labkey/` to generate R image `labkey/rsandbox:latest`.

Note that actual R version might differ based on latest R version at the time the image is built.

To tag the image with the actual R version at the time of build, pass `R_VERSION`, for example: `make rsandbox R_VERSION=4.6.1`.

For more information, see:

https://www.labkey.org/Documentation/wiki-page.view?name=rsandbox
