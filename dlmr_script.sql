CREATE DATABASE proyecto_dlmr;
USE proyecto_dlmr;

CREATE TABLE usuarios(
    id          int(25) auto_increment NOT NULL,
    nombre      varchar(100),
    apellidos   varchar(255),
    consultorio   varchar(255),
    area   varchar(255),
    email       varchar(255) NOT NULL,
    password    varchar(255) NOT NULL,
    fecha       date NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE consultas(
    id int(25) auto_increment NOT NULL,
    usuario_id int(25) NOT NULL,
    paciente varchar(255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha date NOT NULL,
    CONSTRAINT pk_consultas PRIMARY KEY(id),
    CONSTRAINT fk_notas_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;
