Code to Coffee with PL/pgSQL
---

## Prerequisite

1. postgresql (tested with postgresql 13)
2. any postgresql client (this example will use `psql`)

## Instructions

Using containerized postgres instance, this example comes with `docker-compose.yml` for setup local DB instance.

```sh
# make sure port 15432 is not in-use or change port exposed to
# available unused port
# consult with lsof manpage on macOS or ss/netstat for more info
# for example
# lsof -i :15432
# ss -tulpn | grep 15432

# 1. cd into directory with current readme, from root of git repository
cd $(git rev-parse --show-toplevel)/PLpgSQL/choestelus

# 2. bring up postgresql instance
docker-compose up -d

# 3. assuming psql is available in localhost, run migration ordered by name, descending
# log below command is output example.

psql -U postgres -h localhost -p 15432 -f ./1_init.sql

# $ psql -U postgres -h localhost -p 15432 -f 1_init.sql
# Password for user postgres: <refer to docker-compose.yml> which is 'coffee' in this example
# CREATE TABLE
# CREATE TABLE
# CREATE TABLE
# CREATE FUNCTION
# CREATE FUNCTION
# CREATE TRIGGER
# CREATE TRIGGER
# INSERT 0 1
# INSERT 0 1


# 4. run insert data migration to test migrated stored function and triggers
# log below command is output example.

psql -U postgres -h localhost -p 15432 -f ./2_consume_drink.sql

# Password for user postgres: <refer to docker-compose.yml> which is 'coffee' in this example
# psql:2_consume_drink.sql:1: NOTICE:  can i haz java gulp gulp
# psql:2_consume_drink.sql:1: NOTICE:  coding from drinked java
# INSERT 0 1
# INSERT 0 1
# INSERT 0 1
# psql:2_consume_drink.sql:4: NOTICE:  can i haz mocha gulp gulp
# psql:2_consume_drink.sql:4: NOTICE:  coding from drinked mocha
# INSERT 0 1

# 5. (optional) try to look around with changes made in affected tables
psql -U postgres -h localhost -p 15432 -d postgres -c 'select * from public.codes;'
psql -U postgres -h localhost -p 15432 -d postgres -c 'select * from public.drink_entities;'
```
