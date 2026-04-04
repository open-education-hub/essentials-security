FROM ubuntu:18.04

RUN useradd -m -d /home/ctf -s /bin/bash ctf

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo ctf:ctf | chpasswd &&\
    chown -R ctf:ctf /home/ctf/ &&\
    chmod -R 750 /home/ctf/ &&\
    echo 'set +o history' >> /home/ctf/.bashrc

COPY deploy/generate_files.py /home/ctf/generate_files.py
COPY flag /home/ctf/flag

RUN apt-get update && apt-get install -y python3 openssh-server &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    python3 /home/ctf/generate_files.py &&\
    rm /home/ctf/generate_files.py &&\
    rm /home/ctf/flag

ENTRYPOINT service ssh restart && bash
