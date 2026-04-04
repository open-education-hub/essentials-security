FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN chown -R ctf:ctf /home/ctf/
RUN chmod -R 750 /home/ctf/
ADD flag /home/ctf
RUN chmod 440 /home/ctf/flag

COPY src/requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt
RUN mkdir app
RUN mkdir -p  app/templates

COPY src/ /app
