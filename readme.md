# fun-i-con 2023 API

バックエンド班　勉強用

[参考書籍](https://zenn.dev/sh0nk/books/537bb028709ab9)

# 初回の操作
``` shell
docker-compose build
```

``` shell
docker-compose run --entrypoint "poetry install --no-root" demo-app
```

``` shell
docker-compose build --no-cache
```

``` shell
docker-compose up
```

``` shell
docker-compose exec demo-app poetry run python -m api.migrate_db
```

# 二回目以降
``` shell
docker-compose up
```
