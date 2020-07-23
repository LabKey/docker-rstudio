ARG VERSION=3.6.3
FROM rocker/rstudio:${VERSION}

COPY rstudio-singleuser /
RUN dos2unix /rstudio-singleuser; chmod +x /rstudio-singleuser

CMD /rstudio-singleuser $USER
