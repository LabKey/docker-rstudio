FROM docker pull rocker/r-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https apt-utils software-properties-common

RUN apt-get install -y --no-install-recommends build-essential dos2unix libopenblas-dev libssl-dev libxml2-dev nano pandoc procps xvfb x11-common

RUN apt-get install -y --no-install-recommends sudo && \
    apt-get install -y --no-install-recommends  \
	    curl libcurl4-openssl-dev \
        libgd2-xpm-dev libcairo2 libcairo2-dev libxt-dev \
        openssl

## Set a default user. Available via runtime flag `--user docker`
## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
## User should also have & own a home directory.
RUN useradd docker \
	&& mkdir /home/docker \
	&& mkdir /home/docker/R_Sandbox \
	&& chown -R docker /home/docker \
	&& adduser docker staff \
	&& adduser docker sudo \
	&& echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
	&& chmod -R 775 /home/docker


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

COPY install.R /
RUN dos2unix install.R && \
    R --no-site-file -f install.R &&  \
    chmod -R 755 /usr/local/lib/R/site-library

CMD ["/bin/bash"]