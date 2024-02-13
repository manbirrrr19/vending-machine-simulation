FROM arm32v7/python:3.9.18-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

RUN apt-get install -y gcc

RUN pip3 install --upgrade pip -vvv

RUN pip3 install requests -i https://www.piwheels.org/simple

RUN pip3 install smbus==1.1.post2 -vvv -i https://www.piwheels.org/simple

RUN pip3 install setuptools -i https://www.piwheels.org/simple

RUN pip3 install Flask -i https://www.piwheels.org/simple

RUN pip3 install --no-cache-dir rpi.gpio

RUN pip3 install itsdangerous==2.0.1 -i https://www.piwheels.org/simple

RUN pip3 install click -i https://www.piwheels.org/simple

RUN pip3 install Jinja2 -i https://www.piwheels.org/simple

RUN pip3 install MarkupSafe -i https://www.piwheels.org/simple

RUN pip3 install Werkzeug -i https://www.piwheels.org/simple

RUN pip3 install spi==0.2.0 -i https://www.piwheels.org/simple

RUN pip3 install spidev==3.5 -i https://www.piwheels.org/simple


COPY . .

WORKDIR /app/SPI-Py
RUN python3 setup.py install
WORKDIR /app

CMD ["python3", "main.py"]