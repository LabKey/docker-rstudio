ARG VERSION=latest
FROM rocker/rstudio:${VERSION}

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y --no-install-recommends nano procps libxml2-dev xvfb zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY files/conf /etc/cont-init.d/

COPY files/install.R /
RUN R --no-site-file -f install.R &&  \
    chmod -R 755 /usr/local/lib/R/library && \
    chmod -R 755 /usr/local/lib/R/site-library

COPY files/Rprofile.site /Rprofile.site.tmp
RUN cat /Rprofile.site.tmp >> /usr/local/lib/R/etc/Rprofile.site && \
    rm /Rprofile.site.tmp
RUN echo "R_LIBS_USER=~/R/$(R --version | grep -Eo '[0-9]+[.]+[0-9]+')/library" >> /usr/local/lib/R/etc/Renviron

COPY files/cleanupSessionFiles.sh /
RUN chmod 755 /cleanupSessionFiles.sh
