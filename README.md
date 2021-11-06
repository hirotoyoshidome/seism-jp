# SEISM JP
Repository of Statistics of SEISM at Japan.

### SETUP

* Docker

```
cd docker
docker-compose up -d --build
```

* http://127.0.0.1:5000
* http://127.0.0.1:5000/?from=2020-01-02&to=2020-01-03&limit=8

* JS

```
npm ci
npm watch
```

### DATABASE

```
docker exec -it seismjp_mysql bash
mysql -uroot -proot
```

* execute schema.sql queries.

### CREDIT
* [HERE](./CREDITS.md)

### OTHER COMMAND

* delete all unused process.

```
docker rm $(docker ps -q -a)
```

* delete all unused image.

```
docker image prune
```
