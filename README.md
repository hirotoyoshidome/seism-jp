# SEISM JP
Repository of Statistics of SEISM at Japan.

### SETUP

* Docker

```
cd docker
docker-compose up -d --build
```

* http://127.0.0.1:5000
* http://127.0.0.1:5000/?from=2020-01-02&to=2020-01-03

* JS

```
npm ci
```

### DOWNLOAD
* https://openlayers.org/two/
  * unzip donwloaded file.

### DATABASE

```
docker exec -it seismjp_mysql bash
mysql -uroot -proot
```

* execute schema.sql queries.

### OTHER COMMAND

* delete all unused process.

```
docker rm $(docker ps -q -a)
```

* delete all unused image.

```
docker image prune
```
