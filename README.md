# SEISM JP
Repository of Statistics of SEISM at Japan.

### SETUP

* Docker

```
cd docker
docker-compose up -d --build
```

* http://127.0.0.1:5000

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

```
CREATE TABLE `jma` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(255) NULL,
  `lat` varchar(255) NULL,
  `lng` varchar(255) NULL,
  `depth` varchar(255) NULL,
  `magnitude` varchar(255) NULL,
  `date_time` varchar(255) NULL,
  PRIMARY KEY (`id`)
);
```

### OTHER COMMAND

* delete all unused process.

```
docker rm $(docker ps -q -a)
```

* delete all unused image.

```
docker image prune
```
