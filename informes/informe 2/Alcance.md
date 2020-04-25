### Objetivo General

Este proyecto se enfocará en desarrollar un sistema que permita obtener información acerca de la ubicación y el estado físico de las señales de tránsito, por medio de cámaras de video instaladas en los vehículos de el o los clientes que utilicen dicho sistema. Todo esto tendrá la finalidad de permitir una mayor y mejor precisión en el análisis de las señaléticas, disminuyendo los recursos destinados actualmente a esta tarea.

### Objetivos Específicos

- De la totalidad de imágenes recibidas, el sistema deberá interpretar de manera correcta al menos el 90% de ellas.
- La interfaz del sistema deberá ser agradable a usuario y, por sobre todo, deberá ser responsiva.
- 

### Alcance del Proyecto

El sistema se desarrollará en base al lenguaje de programación Python y a su framework Django, por lo que los programadores deberán saber este lenguaje y el uso del framework anteriormente mencionado, mientras que el resto del equipo deberán tener nociones básicas de programación.

El funcionamiento de la aplicación web se limitará a la recepción de imágenes (y posiblemente video) desde una API ya existente, interpretar los datos recibidos y entregar la información al usuario que los esté solicitando. Además, la aplicación deberá guardar un registro de los datos procesados y los usuarios que hayan solicitado dicha información.

Por último, el sistema tendrá un nivel de seguridad tal que, si un usuario no se encuentra registrado y/o con permisos, no podrá ingresar a la aplicación.
