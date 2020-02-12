#!/bin/bash
## NOTE: This configuration avoids installing pip3 globally, revert to global install if errors are encountered.
## ubuntu 18.04
apt update && \
#apt install python3-pip python3-venv && \
apt install -y python3-dev libtool python3-venv && \
python3 -m venv venv && \
source venv/bin/activate && \
python3 -m pip install --upgrade pip && \
python3 -m pip install PyOpenSSL pyota pyota[ccurl] docker-compose
if [ $? = 0 ]; then
    echo Local environment setup successfully.
fi
