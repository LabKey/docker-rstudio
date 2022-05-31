FROM python
ENV LANG=C.UTF-8

RUN pip install jupyterlab
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN ln -fs /usr/share/zoneinfo/America/Los_Angeles/etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

COPY entrypoint exec_runreport_tar execute /
RUN chmod 777 /entrypoint /exec_runreport_tar /execute
ENTRYPOINT /entrypoint_sleep
