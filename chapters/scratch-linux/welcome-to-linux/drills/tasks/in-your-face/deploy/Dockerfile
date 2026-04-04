FROM ubuntu:18.04

RUN useradd -m -d /home/ctf -s /bin/bash ctf

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo ctf:ctf | chpasswd &&\
    chown -R ctf:ctf /home/ctf/ &&\
    chmod -R 750 /home/ctf/ &&\
    echo 'set +o history' >> /home/ctf/.bashrc

COPY flag /home/ctf/flag
RUN chmod 644 /home/ctf/flag &&\
    apt-get update && apt-get install -y openssh-server &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT service ssh restart && bash
