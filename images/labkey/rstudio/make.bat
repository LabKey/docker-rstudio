pushd ..\rstudio-base
CALL .\make.bat %*
popd
docker build -t labkey/rstudio .
