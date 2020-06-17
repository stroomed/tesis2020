Create Table Roles (
 IdRol INT(10) NOT NULL AUTO_INCREMENT,
 nRol VARCHAR(30) NOT NULL,
 PRIMARY KEY (IdRol)
);

Create Table Usuario (
 IdUsuario INT(10) NOT NULL AUTO_INCREMENT,
 nUsuario VARCHAR(50) NOT NULL COMMENT 'nombre',
 aUsuario VARCHAR(50) NOT NULL COMMENT 'apellido',
 eUsuario VARCHAR(100) NOT NULL COMMENT 'email',
 tUsuario INT(9) NOT NULL COMMENT 'telefono',
 rUsuario INT(10) NOT NULL COMMENT 'rol',
 PRIMARY KEY (IdUsuario),
 FOREIGN KEY (rUsuario) REFERENCES Roles(IdRol)
);

Create Table Validar (
 Usuario INT(10) NOT NULL,
 Contrasena VARCAHR(16) NOT NULL,
 PRIMARY KEY (Usuario),
 FOREIGN KEY (rUsuario) REFERENCES Usuario(IdUsuario)
);
