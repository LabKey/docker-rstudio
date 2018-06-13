ARG VERSION=latest
FROM rocker/rstudio:${VERSION}

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y --no-install-recommends dos2unix nano procps libxml2-dev xvfb

COPY conf /etc/cont-init.d/
RUN dos2unix /etc/cont-init.d/conf

COPY install.R /
COPY Rlabkey_2.2.3.tar.gz /
RUN R --no-site-file -f install.R &&  \
    chmod -R 755 /usr/local/lib/R/library && \
    chmod -R 755 /usr/local/lib/R/site-library

COPY Rprofile.site /Rprofile.site.tmp
RUN dos2unix /Rprofile.site.tmp && \
    cat /Rprofile.site.tmp >> /usr/local/lib/R/etc/Rprofile.site && \
    rm /Rprofile.site.tmp
RUN echo "R_LIBS_USER=~/R/$(R --version | grep -Eo '[0-9]+[.]+[0-9]+')/library" >> /usr/local/lib/R/etc/Renviron

COPY cleanupSessionFiles.sh /
RUN dos2unix /cleanupSessionFiles.sh
RUN chmod 755 /cleanupSessionFiles.sh
