FROM ubuntu:18.04

RUN apt-get update \
        && apt-get install -y \
            python3 python3-pip python3-dev \
        && cd /usr/local/bin \
        && ln -s /usr/bin/python3 python \
        && pip3 install --upgrade pip

# Set the locale
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8 
ENV LC_ALL en_US.UTF-8

RUN mkdir /shortenURL
WORKDIR /shortenURL
ADD . /shortenURL/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Set environment variables
ENV FLASK_APP=shortenURL


CMD [ "flask", "run", "--host=0.0.0.0" ]
