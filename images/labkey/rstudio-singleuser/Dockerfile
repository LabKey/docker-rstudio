ARG VERSION=4.0.5
FROM rocker/rstudio:${VERSION}

COPY files/rstudio-singleuser /
RUN chmod +x /rstudio-singleuser

CMD /rstudio-singleuser $USER
