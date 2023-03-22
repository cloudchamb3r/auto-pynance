FROM python:3.11-buster

ENV PATH /root/.local/bin:$PATH

# ta-lib setup
WORKDIR /usr/src/talib
COPY ta-lib-bin.tar .
RUN tar -xf ta-lib-bin.tar
WORKDIR /usr/src/talib/ta-lib
RUN ./configure --prefix=/usr
RUN make && make install 


# install poetry setup
WORKDIR /usr/src/app
COPY . .
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install 
RUN chmod +x ./init.sh
CMD [ "sleep", "infinity" ]