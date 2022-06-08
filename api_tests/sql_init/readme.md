
# 数据库导出
```
pg_dump --column-inserts "host=192.168.2.122 port=5432 user=postgres password=123456 dbname=apiserver"> share/02_api_init.sql
pg_dump --column-inserts "host=192.168.2.122 port=5432 user=postgres password=123456 dbname=iot"> share/03_iot_init.sql

```

# 数据库导入
```
psql "host=192.168.2.122 port=5432 user=postgres password=123456 dbname=apiserver" -f share/02_api_init.sql
psql "host=192.168.2.122 port=5432 user=postgres password=123456 dbname=iot" -f share/03_iot_init.sql
```

# 2022年后停止维护
20220304为机器人组测试验证处理apiserver db 在`default`下`tmp_api_init.sql`