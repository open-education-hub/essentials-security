FROM ubuntu:18.04

RUN useradd -m -d /home/vuln -s /bin/bash vuln

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo vuln:stupid | chpasswd &&\
    chown -R vuln:vuln /home/vuln/ &&\
    chmod -R 750 /home/vuln/ &&\
    echo 'set +o history' >> /home/ctf/.bashrc

COPY flag /home/vuln/flag
RUN chmod 644 /home/vuln/flag &&\
    apt-get update && apt-get install -y openssh-server &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT service ssh restart && bash
