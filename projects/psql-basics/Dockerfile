FROM ubuntu:22.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql
RUN echo "listen_addresses = '*'" >> /etc/postgresql/14/main/postgresql.conf && \
    echo "host all all 0.0.0.0/0 scram-sha-256" >> /etc/postgresql/14/main/pg_hba.conf
USER postgres
CMD /usr/lib/postgresql/14/bin/postgres --config-file=/etc/postgresql/14/main/postgresql.conf
EXPOSE 5432
