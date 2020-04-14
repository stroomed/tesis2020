# Nombre del proyecto
## Anteproyecto

#### Asignatura: Taller de proyecto de Software.
#### Sección: 01.
#### Docente: Cristhian Aguilera.
#### Integrantes: Nicol Quintuy, Gabriel Barría, Fabricio Guzmán y Ricardo Gutiérrez.
#### Fecha de entrega: Miércoles 15 de abril

---

### Índice
1. Resumen
2. Descripción del problema
   - Descripción de la empresa o negocio
   - Problema u oportunidad
   - Descripción del modelo de negocios
   - Descripción de interesados y posibles usuarios
3. Propuesta de solución
   - Requisitos
   - Solución propuesta
   - Estudio de factibilidad
   - Alcances y restricciones
4. Objetivos
   - General
   - Específicos
5. Referencias bibliográficas

---

## Resumen

Inspirados por complementar una aplicacion ya contruida se da inicio al desarrollo de un Software,
el cual tendra como objetivo principal tomar datos de una imagen la cual seran entregadas por un automovil. A su vez cumplira con scannear las calles detallado las fallas en las señales de transito con un informe detallando las que se encuentran en mal estado o bien informar si se cuenta con esas señaleticas, con esto podremos tener la posicion de donde se encuentran dicho desperfecto por medio de una interfaz amigable con el usuario.


En el presente informe se analizará superficialmente de lo que trata el proyecto, dando a conocer el problema al cual está enfocado, la solución para dicho problema, contando con sus respectivas factibilidades, además del alcance y restricciones del proyecto en base a las habilidades de los integrantes del equipo de trabajo y finalizando con los objetivos generales y específicos del proyecto.

---

## Descripción del problema
### Descripción de la empresa o negocio

COVIS SpA es una empresa de base tecnológica, recientemente creada con el objetivo de generar soluciones competitivas en el mercado de la inteligencia artificial, contando con soluciones basadas en visión por computador, IoT y análisis inteligente de datos.

> Comentarios revisión: Falta un organigrama de la empresa. Revisen la ortografía.

### Problema u oportunidad

La empresa ha identificado la necesidad que tienen los municipios de mantener actualizada la información de las señales de tránsito de las calles, por lo que, basados en un desarrollo previo, se nos ha solicitado el crear una aplicación web que permita automatizar el proceso de actualizar dicha información (que en la actualidad se realiza de forma manual).

### Descripción del modelo de negocios

![image](https://user-images.githubusercontent.com/62029314/79279697-93446900-7e7c-11ea-9638-3a4ed24b6aff.PNG)

> Comentarios revisión: El canvas o modelo de negocios, es en relación a la solución completa, incluyendo el detector que desarrolla la empresa, ustedes son solo una parte de este producto. Socios clave: Solutiva, Universidad del Bio-Bio. Recursos claves: Sistema de detección (hardware, incluye cámaras). Segmento de clientes, falta empresas privadas. Actividades claves: Mejora continua algoritmo de detección, seguimiento continuo de normas del transito, informes mensuales con clientes. El flujo de ingresos no tiene sentido, compra no es un ingreso, gastos fijos tampoco, revisar!.

### Descripción de interesados y posibles usuarios

- Co-fundador de la empresa: Cristhian Aguilera, Dr. en ingeniería eléctrica con de 20 años en formulación y desarrollo de proyectos de investigación e innovación en el ámbito industrial.
- Jefa de la empresa: Ángela Castro, emprendedora con estudios de estudios de postgrado en la Universidad Autónoma de Barcelona con experiencia en proyectos de investigación nacionales e internacionales.
- Co-fundador de la empresa: Renato Vergara, Ingeniero industrial, con experiencia en temas de PI y Gestión de la Innovación. Se ha desarrollado como Gestor Tecnológico por varios años y ha participado en diversas empresas y proyectos en el ámbito industrial.

---

## Propuesta de solución
### Requisitos

- Un API desarollada en Python utilizando Django Rest.
- Una solución modular que permita adaptarse a posibles futuros ajustes.
- Software con diseño de patrones Factory.
- Control de acceso a la aplicación.

### Solución propuesta

Automatizar el proceso de la actualización de la información correspondiente al estado de las señales de tráfico de la ciudad, lo cual se logrará por medio del desarrollo de una API que permita interpretar los datos recibidos y se los entregue al usuario ya como información para su uso.

> Comentarios revisión: La solución es con relación al problema, incluye la detección de señales. Ustedes deben mencionar que como parte de la solución completa se restringirán a desarrollar el api de comunicación entre el hardware y el usuario final, definiendo lo que describen anteriormente.

### Estudio de factibilidad

#### Económica

![image](https://user-images.githubusercontent.com/62030014/78712305-6f19e280-78e6-11ea-8567-061f6c235103.png)

![image](https://user-images.githubusercontent.com/62030014/78712332-793be100-78e6-11ea-9f68-4639cc1afae7.png)

Segun el estudio economico, el proyecto al no ser con fines de lucro y solo de caracter educacional no contempla ni una inversion ni ganancia monetaria, solamente conocimiento adquirido por los creadores gracias a la investigación.

> Comentarios revisión: Lo anterior no quita el análisis de factibilidad. Deben ver el proyecto como un todo, y limitarse al desarrollo de tu parte. Osea aunque el desarrollo de ustedes cueste 0, el proyecto debe dar indicios de las ganancias esperadas del servicio y los costos de mantención del mismo. Si no manejan esos datos, deben consultarlos conmigo.


#### Técnica

![image](https://user-images.githubusercontent.com/62029314/79279878-ff26d180-7e7c-11ea-866d-b12f4dae5b7f.PNG)

> Comentarios revisión: Como se relacionan los requerimientos con sus capacidades?. Es posible realizar lo que se pide?

#### Legal

En el ámbito legal, no se encuentra regulado el sacar fotografías o grabar video en la vía pública. 

Sin embargo, en el artículo 19 de la Constitución, N° 4, indica que:

> 4º.- El respeto y protección a la vida privada y a la honra de la persona y su familia, y asimismo, la protección de sus datos personales. El tratamiento y protección de estos datos se efectuará en la forma y condiciones que determine la ley.

Por lo que, en caso de que se utilice la imagen de una persona para publicidad (por ejemplo), esa persona podrá solicitar el no uso de su imagen sin su consentimiento.

#### Riesgos


#### Ventajas y Desventajas




#### Beneficios Tangibles

- Mayor alcance de informacion en cuanto a señaleticas.
- Actualizar Información.

#### Beneficios Intangibles 

- La información será confiable.
- Control y seguimiento de la señales de transito.
- Aprovechar los recursos tecnológicos adquiridos.


#### Conclusión de Factibilidad



### Alcances y restricciones

El desarrollo de esta aplciación se limitará a la creación de la aplicación web que pueda recibir los datos de la API ya existente, trabaje los datos recibidos y le entregue la información al usuario.

Por su parte, la aplicación será desarrollada exclusivamente con Django Rest, por lo que los programadores deberán trabajar únicamente con el lenguaje Python.

El o los testers de la aplicación solo deberán probar por el correcto funcionamiento de la aplicación, por lo que no es estrictamente necesario que ellos sepan python a cabalidad.

---

## Objetivos
### General

Desarrollar un sistema que pueda ser vendido o arrendado a municipios del país, el cual permitirá identificar las señales de tránsito y/o semáforos que estén dañados o, en su defecto, permita identificar lugares en los que sería necesario instalar uno.

> Comentarios revisión: Deben corregir la redacción. Adicionalmente, es necesario responder las 3 preguntas, que? como? para que? . El como no existe en ese objetivo

### Específicos

- Determinar datos que se recibirán de la API.
- Modelar un sistema que pueda trabajar con los datos recibidos.
- Diseñar una interfaz de usuario para el sistema y que incluya un control de inicio de sesión.
- Realizar pruebas para validar el rendimiento de la aplicación.
- Entregar la aplicación finalizada al cliente.

> Comentarios revisión: Lo anterior son tareas no objetivos

---

## Referencias bibliográficas (linkografía)

http://covis.cl

https://www.diarioconcepcion.cl/ciudad/2017/09/25/fotografia-en-la-via-publica-es-legal-que-te-tomen-una-foto-sin-tu-consentimiento.html

https://www.leychile.cl/Navegar?idNorma=242302
