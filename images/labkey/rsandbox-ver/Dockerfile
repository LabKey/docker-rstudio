ARG VERSION=3.6.3
FROM rocker/r-base:${VERSION}

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-transport-https \
        apt-utils \
        software-properties-common \
        build-essential \
        dos2unix \
        libopenblas-dev \
        libxml2-dev \
        pandoc \
        procps \
        sudo \
        curl \
        libcurl4-openssl-dev \
        libcairo2 \
        libcairo2-dev \
        libxt-dev \
        libssl-dev \
        openssl \
        dumb-init \
        r-cran-cairo \
        r-cran-data.table \
        r-cran-ggplot2 \
        r-cran-httr \
        r-cran-knitr \
        r-cran-jsonlite \
        r-cran-plotly \
        r-cran-readr \
        r-cran-rmarkdown \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

## Set a default user. Available via runtime flag `--user docker`
## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
## User should also have & own a home directory.
## Allow sodo usage for user
RUN useradd docker \
    && mkdir /home/docker \
    && mkdir /home/docker/R_Sandbox \
    && chown -R docker:docker /home/docker \
    && adduser docker staff \
    && adduser docker sudo \
    && echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/docker \
    && chmod 0440 /etc/sudoers.d/docker \
    && chmod -R 775 /home/docker


COPY install.R /
RUN dos2unix install.R && \
    R --no-site-file -f install.R &&  \
    chmod -R 755 /usr/local/lib/R/site-library

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
