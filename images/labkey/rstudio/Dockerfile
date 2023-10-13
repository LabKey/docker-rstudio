ARG VERSION=latest
FROM labkey/rstudio-base:${VERSION}

RUN apt-get update && \
    apt-get install -y --no-install-recommends  \
    curl libcurl4-openssl-dev \
        libgd-dev libcairo2 libcairo2-dev libxt-dev pandoc \
        libssl-dev openssl cmake libnlopt-dev libgit2-dev libfontconfig1-dev \
        libharfbuzz-dev libfribidi-dev libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY install.R /
RUN dos2unix install.R && \
    R --no-site-file -f install.R &&  \
    chmod -R 755 /usr/local/lib/R/site-library

COPY extra.R /
RUN dos2unix extra.R && \
    R --no-site-file -f extra.R &&  \
    chmod -R 755 /usr/local/lib/R/site-library

COPY bioConductor.R /
RUN dos2unix bioConductor.R && \
    R --no-site-file -f bioConductor.R &&  \
    chmod -R 755 /usr/local/lib/R/site-library