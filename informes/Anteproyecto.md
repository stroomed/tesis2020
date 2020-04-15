# Nombre del proyecto
## Anteproyecto

#### Asignatura: Taller de proyecto de Software.
#### Sección: 01.
#### Docente: Cristhian Aguilera.
#### Integrantes: Nicol Quintuy, Gabriel Barría, Fabricio Guzmán y Ricardo Gutiérrez.
#### Fecha de entrega: Miércoles 15 de abril

---

### Índice
1. [Resumen](#resumen)
2. [Descripción del problema](#descripción-del-problema)
   - Descripción de la empresa o negocio
   - Problema u oportunidad
   - Descripción del modelo de negocios
   - Descripción de interesados y posibles usuarios
3. [Propuesta de solución](#propuesta-de-solución)
   - Requisitos
   - Solución propuesta
   - Estudio de factibilidad
   - Riesgos
   - Alcances y restricciones
4. [Objetivos](#objetivos)
   - General
   - Específicos
5. [Referencias bibliográficas](#referencias-bibliográficas-linkografía)

---

## Resumen
COVIS SpA una empresa dedicada a generar soluciones tecnológicas en el ámbito de la inteligencia artificial, actualmente se encuentra desarrollando un software el cual es capaz de obtener y analizar datos de imágenes que contengan señales de tránsito, la idea de este proyecto es crear un software que sea capaz de extraer toda esta información a través de imágenes y con ello determinar el estado de las calles, señales de tránsito y su ubicación según el GPS.

Basados en lo anterior es necesaria la implementación de una interfaz gráfica que sea capaz de establecer la comunicación del cliente con el software antes mencionado, por esta razón se ha decidido implementar un api rest que sea capaz de recibir imágenes o videos para luego redireccionarlos al software el cual se encargara de analizarlas y finalmente identificar cada objeto detectado en la imagen, devolviendo los resultados para ser presentados al cliente en forma gráfica a través de una tabla que muestre el estado de las señales de tránsito, ubicación y tipo de señal de transito identificada.

En el presente informe se analizará superficialmente de lo que trata el proyecto, dando a conocer el problema al cual está enfocado, la solución para dicho problema, contando con sus respectivas factibilidades, además del alcance y restricciones del proyecto en base a las habilidades de los integrantes del equipo de trabajo y finalizando con los objetivos generales y específicos del proyecto.

---

## Descripción del problema
### Descripción de la empresa o negocio

COVIS SpA es una empresa de base tecnológica, recientemente creada con el objetivo de generar soluciones competitivas en el mercado de la inteligencia artificial, contando con soluciones basadas en visión por computador, IoT y análisis inteligente de datos.

El organigrama de la empresa sería el siguiente:

![image](https://user-images.githubusercontent.com/62028929/79285792-8f204780-7e8c-11ea-8d55-3b071d9d4525.png)

### Problema u oportunidad

La empresa ha identificado la necesidad que tienen los municipios de mantener actualizada la información de las señales de tránsito de las calles, por lo que, basados en un desarrollo previo, se nos ha solicitado el crear una aplicación web que permita automatizar el proceso de actualizar dicha información (que en la actualidad se realiza de forma manual).

### Descripción del modelo de negocios

![image](https://user-images.githubusercontent.com/62029314/79279697-93446900-7e7c-11ea-9638-3a4ed24b6aff.PNG)

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

Automatizar el proceso de actualización de la información correspondiente al estado en el que se encuentran las señales de tráfico en una ciudad determinada, lo cual se logrará por medio del desarrollo de una API que permita interpretar los datos recibidos y se los entregue al usuario ya como información para su uso.

> Comentarios revisión: La solución es con relación al problema, incluye la detección de señales. Ustedes deben mencionar que como parte de la solución completa se restringirán a desarrollar el api de comunicación entre el hardware y el usuario final, definiendo lo que describen anteriormente.

### Estudio de factibilidad

#### Económica

![image](https://user-images.githubusercontent.com/62030014/79377578-e7595700-7f29-11ea-9698-b27a0ecec83f.png)

El costo para la etapa de investigación equivale a $25.000.000
Por otra parte, para la etapa de implementación, el hardware que incluye cámaras, computador herramientas y material para instalación equivale a $1.300.000
Para la etapa de mantenimiento se añadirán 2 ingenieros cuyos valores mensuales equivalen a $1.500.000 cada uno y también por cada 5 municipalidades que se vayan agregando se añadirá un técnico encargado del mantenimiento del equipo, además los gastos varios que son recursos que pueden llegar a utilizarse de forma fija se estima que su valor anual equivale a $1.140.000 aproximadamente.


![image](https://user-images.githubusercontent.com/62030014/79377590-ede7ce80-7f29-11ea-8c02-397556eba95d.png)

Según el flujo de caja realizado con una proyección para 5 años, en el primer año no se percibirán ganancias, sino hasta el año 2 donde se comenzará a ganar la cantidad de $95.360.000  anuales, esto teniendo en cuenta que en el primer año solo se tendrán el 2% de los municipios lo que equivale a 6, con una subida del 3% por año se estima que cada año se irán agregando 11 municipios de un total de 345 en el país.
La TIR señala que el proyecto es viable en un 213%.


#### Técnica

![image](https://user-images.githubusercontent.com/62029314/79279878-ff26d180-7e7c-11ea-866d-b12f4dae5b7f.PNG)

> Comentarios revisión: Como se relacionan los requerimientos con sus capacidades?. Es posible realizar lo que se pide?

#### Legal

En el ámbito legal, no se encuentra regulado el sacar fotografías o grabar video en la vía pública. 

Sin embargo, en el artículo 19 de la Constitución, N° 4, indica que:

> 4º.- El respeto y protección a la vida privada y a la honra de la persona y su familia, y asimismo, la protección de sus datos personales. El tratamiento y protección de estos datos se efectuará en la forma y condiciones que determine la ley.

Por lo que, en caso de que se utilice la imagen de una persona para publicidad (por ejemplo), esa persona podrá solicitar el no uso de su imagen sin su consentimiento.

#### Ventajas

Los beneficios de la Api estan encaminados a mejorar la informacion que se tienen de las señales de tránsito.
- Reparar señaleticas en mal estado o simplemente las que no se encuentran.
- La API sera unica ya que hasta el momento no hay otra que cumpla con lo mismo que la nuestra.
- Mejorar el viaje en automovil.

#### Desventajas

_agregar desventajas_

#### Beneficios Tangibles

- Mayor alcance de informacion en cuanto a señaleticas.
- Actualizar Información.
- Mayor precisión en el analisis del estado de las señales de transito y calles

#### Beneficios Intangibles 

- La información será confiable.
- Control y seguimiento de la señales de transito.
- Aprovechar los recursos tecnológicos adquiridos.
- Ahorra tiempo y esfuerzo

#### Conclusión de Factibilidad

Al crear la API, los beneficios que se obtienen para la empresa son numerosas y el costo del mismo se recuperan con las ventajas y el ahorro en tiempo y esfuerzo.

El proyecto presenta una solución optima y esta encaminado a generar servicios de calidad y confiables para los clientes.

El costo total correspondiente al funcionamiento de la API seran cobradas por suscripciones mensuales a las entidades ya descritas.

Anteriormente fueron mencionadas la ventajas de la API y por ello se procede a continuar con el desarrollo de esta ya que los resultados del análisis de factibilidad nos indican que el proyecto es viable y factible.

### Riesgos

Durante el desarrollo de la API serán considerados todos los casos posibles por parte del equipo, considerando como riesgos aquellas situaciones en que la API presente fallas y no se recupere.

- La falta de mantenimiento tanto a hardware como a software producirian fallas a futuro por ello se recomienda dar mantenimiento eventualmente.
- La falta de comunicación por parte del grupo podria atrasar el desarrollo de la API.
- La falta de conocimiento en programas que se utilizaran.

### Alcances y restricciones

El desarrollo de este proyecto se limitará a la creación de una interfaz que sea capaz de enviar y recibir datos de la API ya existente, ordenarlos y posteriormente mostrarlos de forma grafica a través de una tabla que contenga toda la información. 

Por su parte, la aplicación será desarrollada exclusivamente con Django Rest, por lo que los programadores deberán trabajar únicamente con el lenguaje Python.

El o los testers de la aplicación solo deberán probar por el correcto funcionamiento de la aplicación, por lo que no es estrictamente necesario que ellos sepan python a cabalidad.

---

## Objetivos
### General

Desarrollar un sistema que permita obtener información acerca del estado y ubicación de las señales de tránsito a través de imágenes captadas por una cámara preinstaladas en un vehículo, con esto lograr una mayor precisión en el análisis del estado de las calles y señaléticas, permitiendo así disminuir tiempo y recursos destinados a esta labor.

### Específicos

- Analizar el 90% de las imágenes 
- Detectar al 90% la cantidad de anomalías que pueda llegar a tener una señal de transito
- Definir ubicación exacta del lugar en el que se encuentra cada señal de transito 

---

## Referencias bibliográficas (linkografía)

http://covis.cl

https://www.diarioconcepcion.cl/ciudad/2017/09/25/fotografia-en-la-via-publica-es-legal-que-te-tomen-una-foto-sin-tu-consentimiento.html

https://www.leychile.cl/Navegar?idNorma=242302
