ARG VERSION=18.04
FROM ubuntu:${VERSION}

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https apt-utils software-properties-common
    
RUN apt-get install -y --no-install-recommends build-essential dos2unix libopenblas-dev libssl-dev libxml2-dev nano pandoc procps xvfb x11-common

# NOTE much faster to use apt to install prebuilt packages than using "install.packages()"
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \ 
    r-base \
    r-cran-bitops \
    r-cran-cairo \
    r-cran-data.table \
    r-cran-digest \
    r-cran-dplyr \
    r-cran-ggplot2 \
    r-cran-htmlwidgets \
    r-cran-httr \
    r-cran-knitr \
    r-cran-jsonlite \
    r-cran-lubridate \
    r-cran-plotly \
    r-cran-rcpp \
    r-cran-rcurl \
    r-cran-readr \
    r-cran-reshape2 \
    r-cran-markdown \
    r-cran-scales \
    r-cran-stringr \
    r-cran-tidyr 

COPY install.R /tmp/
RUN R --vanilla -f /tmp/install.R 

RUN ln -fs /usr/share/zoneinfo/America/Los_Angeles/etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata

RUN R --version
