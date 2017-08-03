##
#  Copyright (c) 2016 LabKey Corporation. All rights reserved. No portion of this work may be reproduced in
#  any form or by any electronic or mechanical means without written permission from LabKey Corporation.
##
install.packages("PKI",repos="http://rforge.net")
install.packages(c(
  "Rlabkey", "Cairo", "ggplot2", "plotly", "httr", "readr", "data.table",
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
