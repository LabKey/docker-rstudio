labkey/rsandbox:latest
======

Dockerfile for building a Dockerized LabKey R image.

Run `./make` to generate R image `labkey/rsandbox:latest`.

The R version is pinned by `ARG VERSION` in the Dockerfile. Override it per-build with `./make --build-arg VERSION=<version>`, but note that tags older than R 4.0 are based on EOL Debian releases whose apt mirrors no longer resolve.

To tag the image with the R version instead of `latest`, change `latest` in the `make` file, for example: `4.5.1`.

For more information, see:

https://www.labkey.org/Documentation/wiki-page.view?name=rsandbox
