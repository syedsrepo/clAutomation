FROM ubuntu:16.04
LABEL description = "haproxy image with collectd"
RUN apt update -y
RUN apt install net-tools -y
RUN apt install netcat -y

RUN apt install rsyslog -y
COPY rsyslog.conf /etc/rsyslog.conf

RUN apt install collectd collectd-utils -y
COPY collectd.conf /etc/collectd/collectd.conf

COPY startup.sh   /usr/local/bin/

RUN apt install haproxy -y
COPY haproxy.cfg /etc/haproxy/haproxy.cfg

COPY docker-entrypoint.sh /usr/local/bin/
COPY startup.sh   /usr/local/bin/


ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["startup.sh"]
