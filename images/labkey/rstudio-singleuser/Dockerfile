ARG VERSION=4.0.5
FROM rocker/rstudio:${VERSION}

COPY rstudio-singleuser /
RUN chmod +x /rstudio-singleuser

CMD /rstudio-singleuser $USER
