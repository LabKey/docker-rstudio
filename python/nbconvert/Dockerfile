FROM python
ENV LANG=C.UTF-8

RUN apt-get update -y && apt-get dist-upgrade -y
RUN apt-get install -y jq

RUN python3 -m pip install --upgrade pip
RUN pip install jupyterlab
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN ln -fs /usr/share/zoneinfo/America/Los_Angeles/etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

RUN mkdir /reportInput

COPY ReportConfig.py /
COPY entrypoint exec_runreport_tar execute /
RUN chmod 777 /entrypoint /exec_runreport_tar /execute
ENTRYPOINT /entrypoint
