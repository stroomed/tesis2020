# Nombre del proyecto
## Anteproyecto

#### Asignatura: Taller de proyecto de Software.
#### Sección: 01.
#### Docente: Cristhian Aguilera.
#### Integrantes: Nicol Quintuy, Gabriel Barría, Fabricio Guzmán y Ricardo Gutiérrez.
#### Fecha de entrega: Martes 15 de abril

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

> En el transcurso de este proyecto se diseñará y se desarrollará un sistema que le permita al usuario el trabajar con señales de tránsito y semáforos, teniendo así la oportunidad de ofrecer su servicio a municipios del país.

   Inspirados por complementar una aplicación ya construida, inicia el desarrollo de un software API el cual tiene como objetivo el tomar datos de una imagen que será entregada por un automóvil, el cual cumplirá con la función de scanner de las calles y así poder tener un informe detallado de las zonas en las que las señales de tráfico se encuentren en mal estado o que simplemente estas no existan donde deberían, dando la posición de donde se encuentra dicho desperfecto por medio de una interfaz agradable con el usuario.
   En el siguiente informe se analizará superficialmente de lo que trata el proyecto, dando a conocer el problema al cual está enfocado, la solución para dicho problema, contando con sus respectivas factibilidades, además del alcance y restricciones del proyecto en base a las habilidades de los integrantes del equipo de trabajo y finalizando con los objetivos generales y específicos del proyecto.


> Comentarios revisión: El resumen no da a entender de que se trata el proyecto, carece de información relevante, descripción del problema, y motivación detrás de la solución. Adicionalmente, no explica en que consiste el actual informe. Revisen la rubrica!

---

## Descripción del problema
### Descripción de la empresa o negocio

COVIS SpA es una empresa de base tecnológica recientemente creada con el objetivo de generar soluciones competitivas en el mercado de la inteligencia artificial con soluciones basados en visión por computador, internet de las cosas y análisis inteligente de datos.

> Comentarios revisión: Falta un organigrama de la empresa. Revisen la ortografía.

### Problema u oportunidad

Se ha presentado la oportunidad de desarrollar una aplicación web que reciba los datos obtenidos desde la API desarrollada anteriormente por la empresa, muestre dicha información y permita su trabajo con ella.

> Comentarios revisión: Esta sección fue mal interpretada. En problema debieron haber descrito la necesidad de mantener actualizada la información de las señales de trafico de las ciudades. La oportunidad tiene relación con que ahora se hace manual y la solución lo hace de manera automática, ahorrando tiempo, .... Ustedes están siendo partes de la solución, por lo que el problema y la oportunidad es la misma

### Descripción del modelo de negocios

https://github.com/stroomed/tesis2020/issues/1#issue-596050674

> Comentarios revisión: Las imágenes pueden ser agregadas a markdown sin tener que ir a  un issue, lean documentación de github o markdown. Dicho lo anterior, el canvas o modelo de negocios, es en relación a la solución completa, incluyendo el detector que desarrolla la empresa, ustedes son solo una parte de este producto. Socios clave: Solutiva, Universidad del Bio-Bio. Recursos claves: Sistema de detección (hardware, incluye cámaras). Segmento de clientes, falta empresas privadas. Actividades claves: Mejora continua algoritmo de detección, seguimiento continuo de normas del transito, informes mensuales con clientes. El flujo de ingresos no tiene sentido, compra no es un ingreso, gastos fijos tampoco, revisar!.

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

Desarrollar una aplicación que reciba los datos del usuario, los envíe a la API existente y permita el trabajar con la información entregada por la API.

> Comentarios revisión: La solución es con relación al problema, incluye la detección de señales. Ustedes deben mencionar que como parte de la solución completa se restringirán a desarrollar el api de comunicación entre el hardware y el usuario final, definiendo lo que describen anteriormente.

### Estudio de factibilidad

#### Económica

![image](https://user-images.githubusercontent.com/62030014/78712305-6f19e280-78e6-11ea-8567-061f6c235103.png)

![image](https://user-images.githubusercontent.com/62030014/78712332-793be100-78e6-11ea-9f68-4639cc1afae7.png)

Segun el estudio economico, el proyecto al no ser con fines de lucro y solo de caracter educacional no contempla ni una inversion ni ganancia monetaria, solamente conocimiento adquirido por los creadores gracias a la investigación.

> Comentarios revisión: Lo anterior no quita el análisis de factibilidad. Deben ver el proyecto como un todo, y limitarse al desarrollo de tu parte. Osea aunque el desarrollo de ustedes cueste 0, el proyecto debe dar indicios de las ganancias esperadas del servicio y los costos de mantención del mismo. Si no manejan esos datos, deben consultarlos conmigo.


#### Técnica

https://github.com/stroomed/tesis2020/issues/2#issue-596059277


> Comentarios revisión: Como se relacionan los requerimientos con sus capacidades?. Es posible realizar lo que se pide?

#### Legal

En el ámbito legal, no se encuentra regulado el sacar fotografías o grabar video en la vía pública. 

Sin embargo, en el artículo 19 de la Constitución, N° 4, indica que:

> 4º.- El respeto y protección a la vida privada y a la honra de la persona y su familia, y asimismo, la protección de sus datos personales. El tratamiento y protección de estos datos se efectuará en la forma y condiciones que determine la ley.

Por lo que, en caso de que se utilice la imagen de una persona para publicidad (por ejemplo), esa persona podrá solicitar el no uso de su imagen sin su consentimiento.

### Alcances y restricciones

El software a desarrollar tendrá como objetivo el poder ofrecerlo a municipios y/o Ministerio de Obras Públicas, sin embargo, también se mantiene la posibilidad de ser ofrecido a constructoras privadas para proyectos inmobiliarios futuros.

Por otro lado, la aplicación solo se limitará a la detección de la existencia o falta de semáforos y otras señaléticas de tránsito, mostrándolo así en la interfaz a desarrollar.

Por último, solo las personas registradas podrán hacer uso de la aplicación, es decir, mientras esté en fase de desarrollo, solo gente de COVIS que cuente con acceso podrá ingresar a ella.

> Comentarios revisión: Definan alcances y restricciones particulares del desarrollo, no del producto.
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
