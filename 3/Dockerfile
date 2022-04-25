FROM ubuntu
RUN apt-get update
RUN apt install telnet -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install requests
USER root
COPY podcount.py /root
WORKDIR /root
CMD ["/root/podcount.py"]
ENTRYPOINT ["python3"]

