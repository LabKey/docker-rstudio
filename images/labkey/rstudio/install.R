##
#  Copyright (c) 2017 LabKey Corporation
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##
install.packages("PKI",repos="http://rforge.net")
install.packages(c(
  "Rlabkey", "Cairo", "ggplot2", "plotly", "httr", "readr", "data.table",
# packages rstudio uses,
  "evaluate",
  "digest",
  "formatR",
  "highr",
  "markdown",
  "yaml",
  "htmltools",
  "caTools",
  "knitr",
  "rmarkdown",
  "RJSONIO",
  "rstudioapi",
  "packrat",
  "rsconnect"
  ),
  repos='https://cran.rstudio.com/')
install.packages(c(
  "latticeExtra",
  "lme4",
  "lmtest",
  "openssl",
  "plotly",
  "plyr",
  "png",
  "readxl",
  "reshape2",
  "RSQLite",
  "stringr",
  "stringi",
  "tidyverse",
  "tibble",
  "tidyr"
  ),
  repos='https://cran.rstudio.com/')
install.packages("BiocManager", repos = "https://cloud.r-project.org")
BiocManager::install(c("flowWorkspace", "CytoML"))
