FROM ubuntu:18.04

RUN useradd -m -d /home/ctf -s /bin/bash ctf

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo ctf:ctf | chpasswd &&\
    chown -R ctf:ctf /home/ctf/ &&\
    chmod -R 750 /home/ctf/ &&\
    echo 'set +o history' >> /home/ctf/.bashrc

COPY src/server /tmp/.server

RUN apt-get update && apt-get install -y python3 xinetd net-tools netcat &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

COPY deploy/xinetd.conf /etc/xinetd.d/they-see-me-running

ENTRYPOINT service xinetd restart && bash
