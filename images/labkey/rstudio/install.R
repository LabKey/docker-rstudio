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
  "Cairo", "ggplot2", "plotly", "httr", "rjson", "jsonlite", "Rcpp", "readr", "data.table",
# packages rstudio uses
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
  repos='http://cran.fhcrc.org/')
install.packages("Rlabkey_2.2.3.tar.gz", repos = NULL, type = "source")
