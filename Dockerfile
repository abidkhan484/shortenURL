FROM ubuntu:18.04

RUN apt-get update \
        && apt-get install -y \
            python3 python3-pip python3-dev \
        && cd /usr/local/bin \
        && ln -s /usr/bin/python3 python \
        && pip3 install --upgrade pip


RUN mkdir /shortenURL
WORKDIR /shortenURL
ADD . /shortenURL/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN export FLASK_APP=shortenURL/application.py
# RUN export LC_ALL=C.UTF-8 && export LANG=C.UTF-8


# ENTRYPOINT ["python3"]

CMD [ "flask", "run" ]
