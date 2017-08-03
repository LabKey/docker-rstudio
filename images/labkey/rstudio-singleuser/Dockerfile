FROM labkey/rstudio

COPY rstudio-singleuser /
RUN dos2unix /rstudio-singleuser; chmod +x /rstudio-singleuser

CMD /rstudio-singleuser $USER
