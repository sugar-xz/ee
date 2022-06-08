
-- ALTER USER postgres WITH PASSWORD '123456';
DROP DATABASE IF EXISTS apiserver;
DROP DATABASE IF EXISTS iot;

-- 创建database 设置owner
create database apiserver with owner postgres ENCODING = 'UTF8';
create database iot with owner postgres ENCODING = 'UTF8';

-- 授权
GRANT ALL PRIVILEGES ON DATABASE apiserver TO postgres;
GRANT ALL PRIVILEGES ON DATABASE iot TO postgres;
