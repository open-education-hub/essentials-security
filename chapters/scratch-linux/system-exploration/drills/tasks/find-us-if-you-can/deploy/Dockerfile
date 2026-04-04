FROM ubuntu:18.04

RUN useradd -m -d /home/ctf -s /bin/bash ctf

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo ctf:ctf | chpasswd &&\
    chown -R ctf:ctf /home/ctf/ &&\
    chmod -R 750 /home/ctf/ &&\
    echo 'set +o history' >> /home/ctf/.bashrc

COPY flag1 /usr/local/lib/flag
RUN chown ctf:ctf /usr/local/lib/flag &&\
    chmod 400 /usr/local/lib/flag

RUN mkdir -p /tmp/.hidden/my/bugs/bunny &&\
    chown ctf:ctf /tmp/.hidden/my/bugs/bunny &&\
    chmod -R 750 /tmp/.hidden/my/bugs/bunny

COPY flag2 /tmp/.hidden/my/bugs/bunny/bugs_bunny.doc

RUN apt-get update && apt-get install -y openssh-server &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT service ssh restart && bash
