### Requerimientos

A partir de las distintas reuniones sostenidas con el cliente, se presentan los requerimientos junto a la especificación correspondiente.

**Comentarios: La tabla estaba mal hecha, la tuve que corregir**

Requerimientos Funcionales
Código | Requerimiento | Especificación
-- | -- | --
RF-01 | Toma de información   de imágenes | Recibir información   proveniente del módulo principal y administrarla.
RF-02 | Historial de   solicitudes de información | Mostrar un historial   sobre las solicitudes que se han hecho al servidor de la API.
RF-03 | Historial asíncrono | La información mostrada por la API no será en base a la cantidad de frames enviadas al servidor, sino las necesarias, en caso de que la solicitud sea un video.
RF-04 | Diseño de sistema   administrativo | La API debe tener   interfaz administrativa, usando el template ![Ejemplo de template](https://user-images.githubusercontent.com/62028929/80891158-4b04b380-8c90-11ea-8b11-81ff1029f587.png) donde se muestran diferentes datos, que en nuestro caso serían de solicitudes al servidor.
RF-05 | Control de acceso   exclusivo de administrador | Un sistema de inicio   de sesión para el Admin
RF-06 | Gráficos en base a   la información recopilada | Gráficos en base a   la información recopilada.

**Comentarios: en los requerimientos funcionales, falta lo conversado la semana pasada.**
Requerimientos no funcionales
Código | Requerimiento | Especificación
-- | -- | --
RNF-01 | Base de datos en   MongoDB para la información | La información de la   detección de imágenes debe ser almacenada en una base de datos no relacional   de MongoDB
RNF-02 | Api en Django Rest | El modulo debe estar   creada en el framework Django Rest
RNF-03 | API modular | La api es un módulo,   una parte de software principal
RNF-04 | Base de datos para   los usuarios | Una base de datos   diferente para el control de Django Rest
RNF-05 | Estándar de calidad | La API debe cumplir con el estándar de calidad 1012-2004 IEEE.
