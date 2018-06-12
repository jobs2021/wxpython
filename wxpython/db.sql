CREATE DATABASE db
go
use db
go
CREATE TABLE usuarios 
(
id int IDENTITY,
nombre VARCHAR(50),
contra VARCHAR(50)
)
go
INSERT into usuarios VALUES('jobs2021','12345')
go
SELECT * from usuarios
