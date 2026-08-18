# Build the LabKey R Docker images.
#
# Usage:
#   make <target> [R_VERSION=<tag>]
#
# Targets:
#   r             labkey/r            (from ubuntu; version is fixed in the Dockerfile)
#   rsandbox      labkey/rsandbox     (from rocker/r-ver:$(R_VERSION))
#   rstudio-base  labkey/rstudio-base (from rocker/rstudio:$(R_VERSION))
#   rstudio       labkey/rstudio      (from labkey/rstudio-base:$(R_VERSION); builds rstudio-base first)
#   all           build every image above
#
# Requires Docker 17.05.0 or greater.

.PHONY: all r rsandbox rstudio-base rstudio

R_VERSION ?= latest

all: r rsandbox rstudio-base rstudio

r:
	docker build -t labkey/r:latest r

rsandbox:
	docker build --build-arg VERSION=$(R_VERSION) -t labkey/rsandbox:$(R_VERSION) rsandbox

rstudio-base:
	docker build --build-arg VERSION=$(R_VERSION) -t labkey/rstudio-base:$(R_VERSION) rstudio-base

rstudio: rstudio-base
	docker build --build-arg VERSION=$(R_VERSION) -t labkey/rstudio:$(R_VERSION) rstudio
