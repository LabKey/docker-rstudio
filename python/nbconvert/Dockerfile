FROM python
ENV LANG=C.UTF-8

RUN pip install jupyterlab
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN ln -fs /usr/share/zoneinfo/America/Los_Angeles/etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

COPY entrypoint_runreport_ipynb /
COPY entrypoint_runreport_tar /
COPY entrypoint_runreport_echo /
COPY entrypoint_sleep /
COPY execute /
RUN chmod 777 /entrypoint_*
RUN chmod 777 /execute
ENTRYPOINT /entrypoint_sleep
