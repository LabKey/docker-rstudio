FROM labkey/rstudio-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends  \
	curl libcurl4-openssl-dev \
        libgd-dev libcairo2 libcairo2-dev libxt-dev pandoc \
        libssl-dev openssl dumb-init && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY install.R /
RUN dos2unix install.R && \
    R --no-site-file -f install.R &&  \
    chmod -R 755 /usr/local/lib/R/site-library

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
