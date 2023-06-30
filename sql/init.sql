-- DB削除
DROP DATABASE IF EXISTS postgres_db;
-- DB作成
CREATE DATABASE postgres_db; 

-- 作成したDBへ切り替え
\c postgres_db

-- ロールの作成
--CREATE ROLE postgres WITH LOGIN PASSWORD 'postgres';

-- 権限追加
-- GRANT ALL PRIVILEGES ON SCHEMA hogeschema TO hoge;