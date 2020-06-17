INSERT INTO Roles (nRol) VALUES ('Administrador');
INSERT INTO Roles (nRol) VALUES ('Usuario');

INSERT INTO Usuario (nUsuario, aUsuario, eUsuario, tUsuario, rUsuario) VALUES ('Cristhian', 'Aguilera', 'cristhian@dominio.cl', 912345678, 1);
INSERT INTO Usuario (nUsuario, aUsuario, eUsuario, tUsuario, rUsuario) VALUES ('Fabricio', 'Guzman', 'fabricio@dominio.cl', 912345678, 2);

INSERT INTO Validar (Usuario, Contrasena) VALUES (1, 'passCristhian');
INSERT INTO Validar (Usuario, Contrasena) VALUES (2, 'passFabricio');
