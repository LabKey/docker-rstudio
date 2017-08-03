FROM labkey/rstudio-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends  \
	r-base r-recommended r-base-dev curl libcurl4-openssl-dev \
        libgd2-xpm-dev libcairo2 libcairo2-dev libxt-dev pandoc \
        libssl-dev openssl 

COPY install.R /
RUN dos2unix install.R; Rscript install.R; chmod -R 755 /usr/local/lib/R/site-library
